var React = require('react')
var ReactDOM = require('react-dom')

var VideoList = React.createClass({
    loadBooksFromServer: function () {
        $.ajax({
            url: this.props.url,
            datatype: 'json',
            cache: false,
            success: function (data) {
                this.setState({ data: data });
            }.bind(this)
        })
    },

    getInitialState: function () {
        return { data: [] };
    },

    componentDidMount: function () {
        this.loadBooksFromServer();
        // setInterval(this.loadBooksFromServer,
        //     this.props.pollInterval)
    },
    render: function () {
        if (this.state.data) {
            console.log('DATA!')
            var videoNodes = this.state.data.map(function (video) {
                return <li> {video.lpid} </li>
            })
        }
        return (
            <div>
                <h1>Video List</h1>
                <ul>
                    {videoNodes}
                </ul>
            </div>
        )
    }
})

ReactDOM.render(<VideoList url='/api/videos' pollInterval={60000} />,
    document.getElementById('container'))
