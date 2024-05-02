import random
from PIL import Image, ImageDraw, ImageFont
#You can only force up to one number per column
FORCED_NUMBERS = [12,25,53]
def main():
  num_sheets = get_sheetnums()
  #FORCED_NUMBERS = get_forced_nums()
  print("Forced Numbers: ") 
  print(FORCED_NUMBERS)
  sheetNum = 1
  print("Losing Cards")
  for _ in range(num_sheets):
    num_cards = 4
    cards = []
    for _ in range(num_cards):
        card = generate_nums(True)
        cards.append(card)
        print('')
        print_nums(card)

    generate_printable_bingo_card(cards,"LoserSheet" + str(sheetNum) + ".png")
    sheetNum += 1
  card = generate_nums(False)
  cards = []
  cards.append(card)
  print('')
  print("Winning Card")
  print_nums(card)
  generate_printable_bingo_card(cards, "WinnerSheet.png")
  
def get_sheetnums():
  while True:
    GET_CARDNUMS = int(input('Enter the number of Bingo card sheets to generate (1-10) Each sheet contains 4 bingo cards: '))
    if GET_CARDNUMS <= 15:
      return GET_CARDNUMS
   # TODO: What happens if user enters something that is not an integer?

def get_forced_nums():
    nums = []
    num = int(input('Enter a number between 1 and 15. If you dont want to force a number in the B column enter 0: '))
    if( not (num == 0) and num in range(1, 16) ):
        nums.append(num)
    num = int(input('Enter a number between 16 and 30. If you dont want to force a number in the I column enter 0: '))
    if( not (num == 0) and num in range(16, 31) ):
        nums.append(num)
    num = int(input('Enter a number between 31 and 45. If you dont want to force a number in the N column enter 0: '))
    if( not (num == 0) and num in range(31, 46) ):
        nums.append(num)
    num = int(input('Enter a number between 46 and 60. If you dont want to force a number in the G column enter 0: '))
    if( not (num == 0) and num in range(46, 61) ):
        nums.append(num)
    num = int(input('Enter a number between 61 and 75. If you dont want to force a number in the O column enter 0: '))
    if( not (num == 0) and num in range(61, 76) ):
        nums.append(num)
    return nums


def generate_nums(forcedNums : bool):

  B = random.sample(range(1, 16), 5)
  I = random.sample(range(16, 31), 5)
  N = random.sample(range(31, 46), 4)
  G = random.sample(range(46, 61), 5)
  O = random.sample(range(61, 76), 5)

  
  for Num in FORCED_NUMBERS:
    
    while (Num in B):
        #print("B:")
        #print(B)
        B = random.sample(range(1, 16), 5)

    while (Num in I):
        #print("I:")
        #print(I)
        I = random.sample(range(16, 31), 5)
    
    while (Num in N):
        #print("N:")
        #print(N)
        N = random.sample(range(31, 46), 4)
    
    while (Num in G):
        #print("G:")
        #print(G)
        G = random.sample(range(46, 61), 5)
    
    while (Num in O):
        #print("O:")
        #print(O)
        O = random.sample(range(61, 76), 5)

  if(forcedNums):
    sample = random.sample(FORCED_NUMBERS,random.randint(1,len(FORCED_NUMBERS)))
    print()
    print(sample)
    for Num in sample:
        if((Num in range(1, 16)) and (Num not in B)):
            index_to_replace = random.randint(0, len(B) - 1)
            B[index_to_replace] = Num
        elif((Num in range(16, 31)) and (Num not in I)):
            index_to_replace = random.randint(0, len(I) - 1)
            I[index_to_replace] = Num
        elif((Num in range(31, 46)) and (Num not in N)):
            index_to_replace = random.randint(0, len(N) - 1)
            N[index_to_replace] = Num
        elif((Num in range(46, 61)) and (Num not in G)):
            index_to_replace = random.randint(0, len(G) - 1)
            G[index_to_replace] = Num
        elif((Num in range(61, 76)) and (Num not in O)):
            index_to_replace = random.randint(0, len(O) - 1)
            O[index_to_replace] = Num
    
  
            
        
             

          


  #Add free space
  N.insert(2,0)
  return [B,I,N,G,O]

def print_nums(card):
  print ('   B   I   N   G   O   ')
  print (f' {card[0][0]:>3} {card[1][0]:>3} {card[2][0]:>3} {card[3][0]:>3} {card[4][0]:>3}')
  print (f' {card[0][1]:>3} {card[1][1]:>3} {card[2][1]:>3} {card[3][1]:>3} {card[4][1]:>3}')
  print (f' {card[0][2]:>3} {card[1][2]:>3} {card[2][2]:>3} {card[3][2]:>3} {card[4][2]:>3}')
  print (f' {card[0][3]:>3} {card[1][3]:>3} {card[2][3]:>3} {card[3][3]:>3} {card[4][3]:>3}')
  print (f' {card[0][4]:>3} {card[1][4]:>3} {card[2][4]:>3} {card[3][4]:>3} {card[4][4]:>3}')



# Define the size of each cell and the margin
CELL_SIZE = 75
MARGIN = 0

def generate_printable_bingo_card(cards, filename):
    # Calculate the size of the image with space for BINGO at the top
    width = 5 * CELL_SIZE + 6 * MARGIN
    height = 6 * CELL_SIZE + 7 * MARGIN

    # Create a new blank image
    if(len(cards) > 1):
        image = Image.new('RGB', ((width * 2 ) + 11, (height * 2) + 11), color='white')
    else:
        image = Image.new('RGB', ((width) + 1, (height) + 1), color='white')
    draw = ImageDraw.Draw(image)

    # Load a font
    font = ImageFont.truetype("C:/Users/Thomas/Downloads/bingo-main/arial.ttf", 35)

    card = cards[0]
    xOffset = 0
    yOffset = 0
    # Draw BINGO at the top
    draw.text(((MARGIN + CELL_SIZE // 3) + xOffset, MARGIN + yOffset +15), "B", fill='black', font=font)
    draw.text(((2 * MARGIN + CELL_SIZE + CELL_SIZE // 2.8) + xOffset, MARGIN + yOffset +15), "I", fill='black', font=font)
    draw.text(((2 * MARGIN + CELL_SIZE + CELL_SIZE // 2.8) + xOffset, MARGIN + yOffset +15), "I", fill='black', font=font)
    draw.text(((3 * MARGIN + 2 * CELL_SIZE + CELL_SIZE // 3.5) + xOffset, MARGIN + yOffset +15), "N", fill='black', font=font)
    draw.text(((4 * MARGIN + 3 * CELL_SIZE + CELL_SIZE // 3.5) + xOffset, MARGIN + yOffset +15), "G", fill='black', font=font)
    draw.text(((5 * MARGIN + 4 * CELL_SIZE + CELL_SIZE // 3.25) + xOffset, MARGIN + yOffset +15), "O", fill='black', font=font)

    font = ImageFont.truetype("C:/Users/Thomas/Downloads/bingo-main/arial.ttf", 20)

    Freefont = ImageFont.truetype("C:/Users/Thomas/Downloads/bingo-main/arial.ttf", 15)

    # Iterate through each cell in the card
    for i, row in enumerate(card):
        for j, num in enumerate(row):
            # Calculate the coordinates of the cell
            x0 = i * (CELL_SIZE + MARGIN) + xOffset
            y0 = ((j + 1) * (CELL_SIZE + MARGIN) + MARGIN ) + yOffset
            x1 = x0 + CELL_SIZE
            y1 = y0 + CELL_SIZE

            if(num == 0):
                                # Draw the cell outline
                draw.rectangle([x0, y0, x1, y1], outline='black')

                # Calculate the position to center the number in the cell
                text_width = draw.textlength("FREE", Freefont)
                text_height = 20
                text_x = x0 + (CELL_SIZE - text_width ) // 2
                text_y = y0 + (CELL_SIZE - text_height) // 2

                # Draw the number in the cell
                draw.text((text_x, text_y), "FREE" , fill='black', font=Freefont)
            else:
            
                # Draw the cell outline
                draw.rectangle([x0, y0, x1, y1], outline='black')

                # Calculate the position to center the number in the cell
                text_width = draw.textlength(str(num), font)
                text_height = 35
                text_x = x0 + (CELL_SIZE - text_width ) // 2
                text_y = y0 + (CELL_SIZE - text_height) // 2

                # Draw the number in the cell
                draw.text((text_x, text_y), str(num), fill='black', font=font)

    if(len(cards) > 1):
        card = cards[1]
        xOffset = width + 5
        yOffset = 0
        # Draw BINGO at the top
        font = ImageFont.truetype("C:/Users/Thomas/Downloads/bingo-main/arial.ttf", 35)
        draw.text(((MARGIN + CELL_SIZE // 3) + xOffset, MARGIN + yOffset +15 ), "B", fill='black', font=font)
        draw.text(((2 * MARGIN + CELL_SIZE + CELL_SIZE // 2.8) + xOffset, MARGIN + yOffset +15), "I", fill='black', font=font)
        draw.text(((2 * MARGIN + CELL_SIZE + CELL_SIZE // 2.8) + xOffset, MARGIN + yOffset +15), "I", fill='black', font=font)
        draw.text(((3 * MARGIN + 2 * CELL_SIZE + CELL_SIZE // 3.5) + xOffset, MARGIN + yOffset +15), "N", fill='black', font=font)
        draw.text(((4 * MARGIN + 3 * CELL_SIZE + CELL_SIZE // 3.5) + xOffset, MARGIN + yOffset +15), "G", fill='black', font=font)
        draw.text(((5 * MARGIN + 4 * CELL_SIZE + CELL_SIZE // 3.25) + xOffset, MARGIN + yOffset +15), "O", fill='black', font=font)

        font = ImageFont.truetype("C:/Users/Thomas/Downloads/bingo-main/arial.ttf", 20)

        Freefont = ImageFont.truetype("C:/Users/Thomas/Downloads/bingo-main/arial.ttf", 15)

        # Iterate through each cell in the card
        for i, row in enumerate(card):
            for j, num in enumerate(row):
                # Calculate the coordinates of the cell
                x0 = i * (CELL_SIZE + MARGIN) + xOffset
                y0 = ((j + 1) * (CELL_SIZE + MARGIN) + MARGIN ) + yOffset
                x1 = x0 + CELL_SIZE
                y1 = y0 + CELL_SIZE

                if(num == 0):
                                    # Draw the cell outline
                    draw.rectangle([x0, y0, x1, y1], outline='black')

                    # Calculate the position to center the number in the cell
                    text_width = draw.textlength("FREE", Freefont)
                    text_height = 20
                    text_x = x0 + (CELL_SIZE - text_width ) // 2
                    text_y = y0 + (CELL_SIZE - text_height) // 2

                    # Draw the number in the cell
                    draw.text((text_x, text_y), "FREE" , fill='black', font=Freefont)
                else:
                
                    # Draw the cell outline
                    draw.rectangle([x0, y0, x1, y1], outline='black')

                    # Calculate the position to center the number in the cell
                    text_width = draw.textlength(str(num), font)
                    text_height = 35
                    text_x = x0 + (CELL_SIZE - text_width ) // 2
                    text_y = y0 + (CELL_SIZE - text_height) // 2

                    # Draw the number in the cell
                    draw.text((text_x, text_y), str(num), fill='black', font=font)

        card = cards[2]
        xOffset = 0
        yOffset = height + 5
        # Draw BINGO at the top
        font = ImageFont.truetype("C:/Users/Thomas/Downloads/bingo-main/arial.ttf", 35)
        draw.text(((MARGIN + CELL_SIZE // 3) + xOffset, MARGIN + yOffset +15), "B", fill='black', font=font)
        draw.text(((2 * MARGIN + CELL_SIZE + CELL_SIZE // 2.8) + xOffset, MARGIN + yOffset +15), "I", fill='black', font=font)
        draw.text(((2 * MARGIN + CELL_SIZE + CELL_SIZE // 2.8) + xOffset, MARGIN + yOffset +15), "I", fill='black', font=font)
        draw.text(((3 * MARGIN + 2 * CELL_SIZE + CELL_SIZE // 3.5) + xOffset, MARGIN + yOffset +15), "N", fill='black', font=font)
        draw.text(((4 * MARGIN + 3 * CELL_SIZE + CELL_SIZE // 3.5) + xOffset, MARGIN + yOffset +15), "G", fill='black', font=font)
        draw.text(((5 * MARGIN + 4 * CELL_SIZE + CELL_SIZE // 3.25) + xOffset, MARGIN + yOffset +15), "O", fill='black', font=font)

        font = ImageFont.truetype("C:/Users/Thomas/Downloads/bingo-main/arial.ttf", 20)

        Freefont = ImageFont.truetype("C:/Users/Thomas/Downloads/bingo-main/arial.ttf", 15)

        # Iterate through each cell in the card
        for i, row in enumerate(card):
            for j, num in enumerate(row):
                # Calculate the coordinates of the cell
                x0 = i * (CELL_SIZE + MARGIN) + xOffset
                y0 = ((j + 1) * (CELL_SIZE + MARGIN) + MARGIN ) + yOffset
                x1 = x0 + CELL_SIZE
                y1 = y0 + CELL_SIZE

                if(num == 0):
                                    # Draw the cell outline
                    draw.rectangle([x0, y0, x1, y1], outline='black')

                    # Calculate the position to center the number in the cell
                    text_width = draw.textlength("FREE", Freefont)
                    text_height = 20
                    text_x = x0 + (CELL_SIZE - text_width ) // 2
                    text_y = y0 + (CELL_SIZE - text_height) // 2

                    # Draw the number in the cell
                    draw.text((text_x, text_y), "FREE" , fill='black', font=Freefont)
                else:
                
                    # Draw the cell outline
                    draw.rectangle([x0, y0, x1, y1], outline='black')

                    # Calculate the position to center the number in the cell
                    text_width = draw.textlength(str(num), font)
                    text_height = 35
                    text_x = x0 + (CELL_SIZE - text_width ) // 2
                    text_y = y0 + (CELL_SIZE - text_height) // 2

                    # Draw the number in the cell
                    draw.text((text_x, text_y), str(num), fill='black', font=font)        
                
        card = cards[3]
        
        xOffset = width + 5
        yOffset = height + 5
        # Draw BINGO at the top
        font = ImageFont.truetype("C:/Users/Thomas/Downloads/bingo-main/arial.ttf", 35)
        draw.text(((MARGIN + CELL_SIZE // 3) + xOffset, MARGIN + yOffset +15), "B", fill='black', font=font)
        draw.text(((2 * MARGIN + CELL_SIZE + CELL_SIZE // 2.8) + xOffset, MARGIN + yOffset +15), "I", fill='black', font=font)
        draw.text(((2 * MARGIN + CELL_SIZE + CELL_SIZE // 2.8) + xOffset, MARGIN + yOffset +15), "I", fill='black', font=font)
        draw.text(((3 * MARGIN + 2 * CELL_SIZE + CELL_SIZE // 3.5) + xOffset, MARGIN + yOffset +15), "N", fill='black', font=font)
        draw.text(((4 * MARGIN + 3 * CELL_SIZE + CELL_SIZE // 3.5) + xOffset, MARGIN + yOffset +15), "G", fill='black', font=font)
        draw.text(((5 * MARGIN + 4 * CELL_SIZE + CELL_SIZE // 3.25) + xOffset, MARGIN + yOffset +15), "O", fill='black', font=font)

        font = ImageFont.truetype("C:/Users/Thomas/Downloads/bingo-main/arial.ttf", 20)

        Freefont = ImageFont.truetype("C:/Users/Thomas/Downloads/bingo-main/arial.ttf", 15)

        # Iterate through each cell in the card
        for i, row in enumerate(card):
            for j, num in enumerate(row):
                # Calculate the coordinates of the cell
                x0 = i * (CELL_SIZE + MARGIN) + xOffset
                y0 = ((j + 1) * (CELL_SIZE + MARGIN) + MARGIN ) + yOffset
                x1 = x0 + CELL_SIZE
                y1 = y0 + CELL_SIZE

                if(num == 0):
                                    # Draw the cell outline
                    draw.rectangle([x0, y0, x1, y1], outline='black')

                    # Calculate the position to center the number in the cell
                    text_width = draw.textlength("FREE", Freefont)
                    text_height = 20
                    text_x = x0 + (CELL_SIZE - text_width ) // 2
                    text_y = y0 + (CELL_SIZE - text_height) // 2

                    # Draw the number in the cell
                    draw.text((text_x, text_y), "FREE" , fill='black', font=Freefont)
                else:
                
                    # Draw the cell outline
                    draw.rectangle([x0, y0, x1, y1], outline='black')

                    # Calculate the position to center the number in the cell
                    text_width = draw.textlength(str(num), font)
                    text_height = 35
                    text_x = x0 + (CELL_SIZE - text_width ) // 2
                    text_y = y0 + (CELL_SIZE - text_height) // 2

                    # Draw the number in the cell
                    draw.text((text_x, text_y), str(num), fill='black', font=font)


    # Save the image to a file
    image.save(filename)

main ()