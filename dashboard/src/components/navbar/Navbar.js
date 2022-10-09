import React from 'react'
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import './Navbar.scss';
import {Link} from 'react-router-dom'
import * as Constants from './../../Constants';

function Navbar() {
    const companies = {
        "Adobe Inc." : "ADBE",
        "ADP" : "ADP",
        "AMD" : "AMD",
        "Analog Devices" : "ADI" ,
        "Ansys" : "ANSS",
        "Apple Inc." : "AAPL",
        "Applied Materials" : "AMAT",
        "ASML Holding" : "ASML",
        "Atlassian" : "TEAM",
        "Autodesk" : "ADSK",
        "Broadcom Inc." : "AVGO",
        "Cadence Design Systems" : "CDNS", 
        "Cisco" : "CSCO",
        "Cognizant" : "CTSH",
        "CrowdStrike" : "CRWD",
        "Datadog" : "DDOG",
        "DocuSign" : "DOCU",
        "Fiserv" : "FISV",
        "Fortinet" : "FTNT",
        "Intel" : "INTC",
        "Intuit" : "INTU",
        "KLA Corporation" : "KLAC", 
        "Lam Research" : "LRCX",
        "Marvell Technology" : "MRVL",
        "Microchip Technology" : "MCHP",
        "Micron Technology" : "MU",
        "Microsoft" : "MSFT",
        "Nvidia" : "NVDA",
        "NXP" : "NXPI",
        "Okta, Inc." : "OKTA",
        "Palo Alto Networks" : "PANW", 
        "Paychex" : "PAYX",
        "PayPal" : "PYPL",
        "Qualcomm" : "QCOM",
        "Skyworks Solutions" : "SWKS", 
        "Splunk" : "SPLK",
        "Synopsys" : "SNPS",
        "Texas Instruments" : "TXN",
        "Verisign" : "VRSN",
        "Workday, Inc." : "WDAY",
        "Zoom Video Communications" : "ZM", 
        "Zscaler" : "ZS",
    }

    return (
        <div className='navbar'>
            <Form.Select aria-label="Default select example">
                <option>Select Company</option>

                {Object.keys(companies).map((key,val)=>{
                    return (
                        <option key={val} value={val}>{key}</option>
                    )
                })}
            </Form.Select>
            <Link to={Constants.HOME_ROUTE}>
                <Button variant="primary">Home</Button>
            </Link>
            <Link to={Constants.INDICATOR_ROUTE}>
                <Button variant="primary">Key Performance Indicators</Button>
            </Link>
            <Button variant="primary">Investor Relations</Button>
            <Button variant="primary">Company Environment</Button>

        </div>
    )
}

export default Navbar