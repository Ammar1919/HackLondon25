// import React from 'react'
import "../../../App.css"
import OrganIdFetcher from "../../OrganIDFetcher"
import UrgentOrgan from "../../UrgentOrgan"
import UrgentPatient from "../../UrgentPatient"

const Urgency = () => {
  return (
    <div>
      <h1 className="urgency">URGENCY</h1>
      <OrganIdFetcher/>
      <UrgentPatient/>
      <UrgentOrgan/>
    </div>
  )
}

export default Urgency