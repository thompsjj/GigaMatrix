import h5py
import os



class gigaMatrix2D:
	def __init__(self, nrows, ncols, name=None):
		self.nrows = nrows
		self.ncols = ncols
		if name is None:
			self.name = 'gm2D_%s.hdf5' % (np.random.randint(99999))
		else:
			self.name = name
		self.file = h5py.File(self.name, 'a')
		
		self.entry = self.file.create_dataset('%s_%s'%(nrows,ncols), (nrows, ncols), 'f')
		self.entry = np.zeros((nrows,ncols))

	def __getitem__(self, (x,y)):
		return self.entry[x,y]	

	def __setitem__(self, (x,y), item):
		self.entry[x,y] = item

	def __str__(self):
		return "GM %s: %s x %s" % (self.name, self.nrows, self.ncols)

	def __del__(self):
		self.file.close()



class gigaMatrix3D:
	def __init__(self, nblocks, nrows, ncols, name=None):
		self.nblocks = nblocks
		self.nrows = nrows
		self.ncols = ncols
		if name is None:
			self.name = 'gm3D_%s.hdf5' % (np.random.randint(99999))
		else:
			self.name = name
		self.file = h5py.File(self.name, 'a')
		
		self.entry = self.file.create_dataset('%s_%s_%s'%(nblocks, nrows, ncols), (nblocks, nrows, ncols), 'f')
		self.entry = np.zeros((nblocks,nrows,ncols))

	def __getitem__(self, (x,y,z)):
		return self.entry[x,y,z]	

	def __setitem__(self, (x,y,z), item):
		self.entry[x,y,z] = item

	def __str__(self):
		print "GM %s: %s x %s x %s" % (self.name, self.nblocks, self.nrows, self.ncols)

	def __del__(self):
		self.file.close()




class gigaHisto2D_1C:
	def __init__(self, nrows, ncols, nhisto, name=None):
		self.nrows = nrows
		self.ncols = ncols
		self.nhisto = nhisto
		if name is None:
			self.name = 'gh2D_1C_%s.hdf5' % (np.random.randint(99999))
		else:
			self.name = name
		self.file = h5py.File(self.name, 'a')
		self.entry = []
		for i in xrange(nrows):
			self.entry.append([])
			for j in xrange(ncols):
				self.entry[i].append(self.file.create_dataset('%s_%s'%(i,j), (nhisto,), 'f'))

		self.entry = np.asarray(self.entry)

		for i in xrange(nrows):
			for j in xrange(ncols):
				self.entry[i, j][:] = np.zeros((nhisto,))

	def __getitem__(self, (x,y)):
		return self.entry[x, y]

	def __setitem__(self, (x,y), item):
		self.entry[x,y] = item

	def __str__(self):
		return "GM %s: %s x %s (%s)" % (self.name, self.nrows, self.ncols, self.nhisto)

	def __del__(self):
		self.file.close()

		
		
class gigaHisto3D_1C:
	def __init__(self, nblocks, nrows, ncols, nhisto, name=None):
		self.nblocks = nblocks
		self.nrows = nrows
		self.ncols = ncols
		self.nhisto = nhisto
		if name is None:
			self.name = 'gh3D_1C_%s.hdf5' % (np.random.randint(99999))
		else:
			self.name = name
		self.file = h5py.File(self.name, 'a')
		self.entry = []
		for i in xrange(nblocks):
			self.entry.append([])
			for j in xrange(nrows):
				self.entry[i].append([])
				for k in xrange(ncols):
					self.entry[i][j].append(self.file.create_dataset('%s_%s_%s'%(i,j, k), (nhisto,), 'f'))

		self.entry = np.asarray(self.entry)

		for i in xrange(nblocks):
			for j in xrange(nrows):
				for k in xrange(ncols):
					self.entry[i, j, k][:] = np.zeros((nhisto,))

	def __getitem__(self, (x,y,z)):
		return self.entry[x, y, z]

	def __setitem__(self, (x,y,z), item):
		self.entry[x,y,z] = item

	def __str__(self):
		return "GM %s: %s x %s x %s (%s)" % (self.name, self.nblocks, self.nrows, self.ncols, self.nhisto)

	def __del__(self):
		self.file.close()
	
		

class gigaHisto3D_2C:
	def __init__(self, nblocks, nrows, ncols, nhistoA, nhistoB, name=None):
		self.nblocks = nblocks
		self.nrows = nrows
		self.ncols = ncols
		self.nhistoA = nhistoA
		self.nhistoB = nhistoB
		if name is None:
			self.name = 'gh3D_2C_%s.hdf5' % (np.random.randint(99999))
		else:
			self.name = name
		self.file = h5py.File(self.name, 'a')
		self.entry = []
		for i in xrange(nblocks):
			self.entry.append([])
			for j in xrange(nrows):
				self.entry[i].append([])
				for k in xrange(ncols):
					self.entry[i][j].append(self.file.create_dataset('%s_%s_%s'%(i,j, k), (nhistoA, nhistoB), 'f'))

		self.entry = np.asarray(self.entry)

		for i in xrange(nblocks):
			for j in xrange(nrows):
				for k in xrange(ncols):
					self.entry[i, j, k][:,:] = np.zeros((nhistoA, nhistoB))

	def __getitem__(self, (x,y,z)):
		return self.entry[x,y,z]

	def __setitem__(self, (x,y,z), item):
		self.entry[x,y,z] = item

	def __str__(self):
		return "GM %s: %s x %s x %s (%s x %s)" % (self.name, self.nblocks, self.nrows, self.ncols, self.nhistoA, self.nhistoB)

	def __del__(self):
		self.file.close()

