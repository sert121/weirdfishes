import {
  Box,
  Button,
  Flex,
  Img,
  Spacer,
  Text,Input,
  VStack,
  useMediaQuery,
} from '@chakra-ui/react';
import React from 'react';

const Hero = () => {
  const [isLargerThanLG] = useMediaQuery('(min-width: 70em)');
  return (
    <Flex
      alignItems="center"
      w="full"
      px={isLargerThanLG ? '16' : '6'}
      py="64" 
      minHeight="100vh"
      flexDirection={isLargerThanLG ? 'column' : 'row'}
    >
      <VStack w="50vw">      
         <Input placeholder='type out a song' size='lg' />
      </VStack>
    </Flex>
  );
};

export default Hero;