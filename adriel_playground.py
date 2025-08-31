import networkx as nx
from networkx import PlanarEmbedding

def play_game():
    import catan_engine as ce
    
    
    # player1 = ce.Bot(name="bot1", algorithm=my_method)
    player2 = ce.Person(name="Uriel")
    players = ce.Players( players=[ ce.Person( input("Name:") ) for i in range( int( input("Num Players:") ) ) ] )
    board = ce.Board()
    ce.show(board.nx_board)
    game = ce.Game(players=players, board=board)
    
    game.set_up()
    game.play()


play_game()

#ce.play()

#def get_faces(embedding):
#    """Returns a list of faces, each face is a list of directed edges."""
#    seen_half_edges = set()
#    faces = []
#
#    for u in embedding:
#        print(u)
#        for v in embedding[u]:
#            print(v)
#            if (u, v) not in seen_half_edges:
#                # Walk around the face to the right of (u, v)
#                face = embedding.traverse_face(u, v)
#                faces.append(face)
#                print(face)
#                # Mark all directed edges in the face as seen
#                for i in range(len(face)):
#                    a, b = face[i], face[(i+1) % len(face)]
#                    seen_half_edges.add((a, b))
#                    print(a,b)
#        print()
#    return faces
#
#
#board = ce.Board(size=3)
#board.make_board()
#
## planar_bool, plane_board_embedding = nx.check_planarity(board.nx_board)
## regions = get_faces(plane_board_embedding)
## print(type(regions[0]))
#
#board.get_tiles()
#print(type(board.tiles))
#for tile in board.tiles:
#    #to_show = ""
#    print(tile)
#    print()
#    #for intersection in tile.intersections:
#    #    to_show += str(intersection) + "  "
#    #print(to_show)
#ce.show(board.nx_board)



