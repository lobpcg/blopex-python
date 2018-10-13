function blockVectorZ = matlabCopyMultiVector(blockVectorX,maskX,...
    blockVectorY,maskY)

blockVectorY(:,maskY) = blockVectorX(:,maskX);
blockVectorZ = blockVectorY;


function blockVectorZ = matlabMultiAxpy(blockVectorX,maskX,...
    blockVectorY,maskY,alpha)

if any(size(alpha)~=1)
    error('alpha must be scalar')
end
blockVectorY(:,maskY) = blockVectorY(:,maskY) + ...
  blockVectorX(:,maskX)*alpha;
blockVectorZ = blockVectorY;


function matrix = matlabMultiInnerProd (blockVectorX,maskX,...
    blockVectorY,maskY)
    

% if size(blockVector1In,1)~=size(blockVector1In,1)
%     error('multivector heights are different')
% end

matrix = blockVectorX(:,maskX)'*blockVectorY(:,maskY);


function values = matlabMultiInnerProdDiag(blockVectorX,maskX,...
    blockVectorY,maskY)

values = dot(blockVectorX(:,maskX),blockVectorY(:,maskY))';


function blockVectorZ = matlabMultiMatVec(blockVectorX,maskX,...
  blockVectorY,maskY,operator)

if ~ischar(operator)
  blockVectorY(:,maskY)=operator*blockVectorX(:,maskX);
else
  blockVectorY(:,maskY) = feval(operator,blockVectorX(:,maskX));
end

blockVectorZ = blockVectorY;

function blockVectorZ = matlabMultiVectorByDiag(blockVectorX,maskX,...
    blockVectorY,maskY, values)

matrix = diag(values);
blockVectorY(:,maskY) = blockVectorX(:,maskX)*matrix;
blockVectorZ = blockVectorY;


function blockVectorZ = matlabMultiVectorByMatrix(blockVectorX,maskX,...
    blockVectorY,maskY, matrix)

blockVectorY(:,maskY) = blockVectorX(:,maskX)*matrix;
blockVectorZ = blockVectorY;

