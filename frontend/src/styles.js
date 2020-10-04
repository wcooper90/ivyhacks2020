import styled from 'styled-components'

export const MetaContainer = styled.div`
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;

`

export const MediumContainer = styled.div`
  max-width: 1024px;
  position: relative;
  display: grid;
  width: 100%;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  justify-content: center;
  align-content: center;
  justify-items: center;
  align-items: center; 
  padding: 60px 20px; 
`

export const AboutDescription = styled.div`
  position: relative;
  display: grid;
  width: 100%;
  backgroundcolor: "green";
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  justify-content: center;
  align-content: center;
  padding: 80px 0px; 
`

export const Header1 = styled.h1`
    color: #2b2e32;
`

export const Details = styled.p`
    margin: 2rem 0; 
    color: rgba(43,46,50,.85); 
    line-height: 1.5715;
`

export const HeaderImage = styled.img`
  width: 100%;
  max-width: 400px;
  height: auto;
  align-self: center;
  justify-self: center;
  padding: 20px;
`

export const Button = styled.button`
    padding: 8px 20px; 
    border-radius: 4px; 
    background-color: #ef8354;
    border: none; 
    color: #ffffff; 
    font-size: 16px; 
    box-shadow: 0 2px 0 rgba(0,0,0,.045);
    height: 40px;  
    font-weight: 600; 
  `
