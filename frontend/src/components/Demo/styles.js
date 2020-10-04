import styled from 'styled-components'


export const Button = styled.button`
  padding: 8px 20px;
  border-radius: 4px;
  background-color: #4f5d75;
  margin-left: 20px;
  border: none;
  color: #ffffff;
  font-size: 16px;
  box-shadow: 0 2px 0 rgba(0,0,0,.045);
  height: 40px;
  font-weight: 600;
`


export const TextArea = styled.textarea`
  height: 75%;
  rows: 25;
  cols: 60;
  placeholder: "Type or Paste in Text... "
`;


export const Container = styled.div`
    width: 80%;
    margin: auto;
    display: flex;
    justify-content: center;
`

export const NavItem = styled.p`
font-size: 16px;
position: relative;
margin: 0px;
margin-left: 20px;
margin-right: 20px;
transition: 0.2s;
width: fit-content;
border-bottom: 2px solid white;
text-align: center;

&:hover {
    border-bottom: 2px solid #ef8354;
    cursor: pointer;

}

&:hover a {
  color: rgba(31, 45, 61, 1);
}
`;
