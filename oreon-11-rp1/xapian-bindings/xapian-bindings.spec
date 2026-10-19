%global source0_hash abf46acd62b9647157f36b636e1844e7e3bd9457e42312c40029ed63c602379c
%global tcl_version 8.6
%global tcl_sitearch %{_libdir}/tcl%{tcl_version}
Name:          xapian-bindings
Version:       1.4.30
Release:        1%{?dist}
Summary:        Bindings for the Xapian Probabilistic Information Retrieval Library
License:       GPL-2.0-or-later
URL:           https://www.xapian.org/
Source0:        https://www.oligarchy.co.uk/xapian/%{version}/%{name}-%{version}.tar.xz
%{?filter_setup}
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  libuuid-devel
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
BuildRequires:  ruby
BuildRequires:  ruby-devel
BuildRequires:  rubygem-json
BuildRequires:  rubygem-rdoc
BuildRequires:  rubygems
BuildRequires:  tcl-devel
BuildRequires:  xapian-core-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
Xapian is an Open Source Probabilistic Information Retrieval Library. It
offers a highly adaptable toolkit that allows developers to easily add advanced
indexing and search facilities to applications. This package provides the
files needed for scripts which use Xapian.

%package -n python3-xapian
Summary:       Python 3 bindings for Xapian
Requires:      %{name} = %{version}-%{release}
%{?python_provide:%python_provide python3-xapian}
%description -n python3-xapian
Xapian is an Open Source Probabilistic Information Retrieval framework. It
offers a highly adaptable toolkit that allows developers to easily add advanced
indexing and search facilities to applications. This package provides the
bindings needed for developing Python3 scripts which use Xapian.

%package ruby
Summary:       Files needed for developing Ruby scripts which use Xapian
Requires:      %{name} = %{version}-%{release}
Requires:      ruby-libs
%description ruby
Xapian is an Open Source Probabilistic Information Retrieval framework. It
offers a highly adaptable toolkit that allows developers to easily add advanced
indexing and search facilities to applications. This package provides the
files needed for developing Ruby scripts which use Xapian

%package -n tcl-xapian
Summary:       Files needed for developing TCL scripts which use Xapian
Requires:      %{name} = %{version}-%{release}
Requires:      tcl >= %{tcl_version}
%description -n tcl-xapian
Xapian is an Open Source Probabilistic Information Retrieval framework. It
offers a highly adaptable toolkit that allows developers to easily add advanced
indexing and search facilities to applications. This package provides the
files needed for developing TCL scripts which use Xapian

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# There is no sphinx.main in Sphinx 2
sed -i 's/sphinx\.main/sphinx.cmd.build.main/g' $(grep -r 'sphinx\.main' -l)
sed -i 's/import sphinx/import sphinx.cmd.build/g' $(grep -r 'import sphinx' -l)

%build

export PYTHON3_LIB=%{python3_sitelib}
export RUBY_LIB=%{ruby_vendorlibdir}
export RUBY_LIB_ARCH=%{ruby_vendorarchdir}
export TCL_LIB=%{tcl_sitearch}
%configure --with-python3 --with-ruby --with-tcl
%{make_build}
%install
%{make_install}
rm -rf %{buildroot}%{_datadir}/doc/%{name}
%oreon_autofiles python3-xapian usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles tcl-xapian usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%files -f %{oreon_filedir}/main.list
%files -n python3-xapian -f %{oreon_filedir}/python3-xapian.list
%files -n xapian-bindings-ruby -f %{oreon_filedir}/xapian-bindings-ruby.list
%files -n tcl-xapian -f %{oreon_filedir}/tcl-xapian.list

%changelog

%autochangelog
