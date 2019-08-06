import React from 'react';
import Autocomplete from 'react-autocomplete';

import './App.css';

export default class App extends React.Component {

    constructor(props, context) {
        super(props, context);

        this.state = {
            value: "",
            autocompleteData: [],
            selected_item: {}
        };

        this.onChange = this.onChange.bind(this);
        this.onSelect = this.onSelect.bind(this);
        this.getItemValue = this.getItemValue.bind(this);
        this.renderItem = this.renderItem.bind(this);
        this.retrieveDataAsynchronously = this.retrieveDataAsynchronously.bind(this);
    }


    retrieveDataAsynchronously(searchText){
        let _this = this;
        let url = `/movie/search?key=${searchText}`;
        let xhr = new XMLHttpRequest();
        xhr.open('GET', url, true);
        xhr.responseType = 'json';
        xhr.onload = () => {
            let status = xhr.status;

            if (status === 200) {
                if("Search" in xhr.response){
                    _this.setState({
                        autocompleteData: xhr.response.Search
                    });
                }
            } else {
                console.error("Cannot load data from remote source");
            }
        };

        xhr.send();
    }

    onChange(e){
        this.setState({
            value: e.target.value
        });

        this.retrieveDataAsynchronously(e.target.value);

        console.log("The Input Text has changed to ", e.target.value);
    }

    onSelect(val){
        this.setState({
            value: val
        });

        console.log("Option from 'database' selected : ", val);
    }


    renderItem(item, isHighlighted){
        return (
            <div key={ item.imdbID } className={`item ${isHighlighted ? 'item-highlighted' : ''}`}>
                {item.Title}
            </div>   
        ); 
    }


    getItemValue(item){
        let url = `/movie/details/${item.imdbID}`;
        fetch(url)
        .then(res => res.json())
        .then(
            (result) => {
                this.setState({
                    selected_item: result.fields
                });
            }
        )
        return `${item.Title}`;
    }

    render() {
        return (
          <div className="wrap">
            <div className="search">
            <label>Seach Movie Name</label>&nbsp;
                  <Autocomplete
                    getItemValue={this.getItemValue}
                    items={this.state.autocompleteData}
                    renderItem={this.renderItem}
                    value={this.state.value}
                    onChange={this.onChange}
                    onSelect={this.onSelect}
                    className="searchTerm"
                />
                
            </div>

            <div className="DetailsSection">
                <label>Title: {this.state.selected_item.title}</label>
                <label>Rated: {this.state.selected_item.rated}</label>
                <label>Actors: {this.state.selected_item.actors}</label>
            </div>
            
               
            </div>
        );
    }
}