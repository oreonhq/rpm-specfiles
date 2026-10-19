%global source0_hash c6b1b3550881e57ebe530cc6cffefc87cd9bf49c30b37b894065a9f810875e46
Name:           python-Rtree
Version:        1.4.1
Release:        1%{?dist}
Summary:        R-Tree spatial index for Python GIS
%global debug_package %{nil}
License:        MIT
URL:            https://github.com/Toblerity/rtree
Source0:        https://files.pythonhosted.org/packages/source/r/rtree/rtree-%{version}.tar.gz
Patch:          0001-Treat-as-pure-Python-since-libspatialindex-is-not-bu.patch
%global common_description %{expand:
Rtree is a ctypes Python wrapper of libspatialindex that provides a number of
advanced spatial indexing features for the spatially curious Python user. These
features include:
  • Nearest neighbor search
  • Intersection search
  • Multi-dimensional indexes
  • Clustered indexes (store Python pickles directly with index entries)
  • Bulk loading
  • Deletion
  • Disk serialization
  • Custom storage implementation (to implement spatial indexing in ZODB, for
    example)}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61
Requires:       python3-Rtree = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-rtree
Summary:        R-Tree spatial index for Python GIS
BuildArch:      noarch
Requires:       spatialindex
%description -n python3-rtree %{common_description}

%prep
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-rtree usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pytest --doctest-modules tests rtree
%files
%files -n python3-rtree -f %{oreon_filedir}/python3-rtree.list

%changelog

%autochangelog
