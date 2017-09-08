import React from "react";

import { gql, graphql } from "react-apollo";

const Page = gql`
  query Page {
    pages {
      title
    }
  }
`;

const PagesList = ({ data }) => {
  if (data.loading) {
    return <div>Loading...</div>;
  }

  return (
    <ul>{data.pages.map(page => <li key={page.title}>{page.title}</li>)}</ul>
  );
};

const PagesListWithData = graphql(Page)(PagesList);

export default PagesListWithData;
