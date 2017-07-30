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
                return (
                    <tr key={video.apn}>
                        <td> {video.name} </td>
                        <td> {video.session_year}</td>
                        <td> {video.category} </td>
                        <td> {video.referenceid} </td>
                        <td> {video.referencetype}</td>
                    </tr>)
            })
        }
        return (
            <tbody>
              {videoNodes}
            </tbody>
        )
    }
})

ReactDOM.render(<VideoList url='/api/videos' pollInterval={60000} />,
    document.getElementById('container'))
