%global source0_hash b22ead7da80fa1735291b2d83198adf41bf36101e4fcb2c4f07c1cfacf211c75

# Setup _pkgdocdir if not defined already.
%{!?_pkgdocdir:%global _pkgdocdir %{_docdir}/%{name}-%{version}}

%global lc_name colpack
%global giturl  https://github.com/CSCsw/%{name}

Name:           ColPack
Version:        1.0.10
Release:        29%{?dist}
Summary:        Algorithms for specialized vertex coloring problems

License:        LGPL-3.0-or-later
URL:            http://cscapes.cs.purdue.edu
Source0:        %{giturl}/archive/v1.0.10.tar.gz#/%{name}-%{version}.tar.gz

Patch0:         ColPack-CVE-2024-55566.patch

BuildRequires:  chrpath
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make

Provides:       %{lc_name}               = %{version}-%{release}
Provides:       %{lc_name}%{?_isa}       = %{version}-%{release}

%description
ColPack is a package comprising of implementation of algorithms for
specialized vertex coloring problems that arise in sparse derivative
computation. It is written in an object-oriented fashion heavily using
the Standard Template Library (STL).  It is designed to be simple,
modular, extendable and efficient.

%package cli
Summary:        CLI-tool for %{name}

Requires:       %{name}%{?_isa}          = %{version}-%{release}

Provides:       %{lc_name}-cli           = %{version}-%{release}
Provides:       %{lc_name}-cli%{?_isa}   = %{version}-%{release}

%description cli
This package contains a cli-tool for %{name}

%package devel
Summary:        Development files for %{name}

Requires:       %{name}%{?_isa}          = %{version}-%{release}

Provides:       %{lc_name}-devel         = %{version}-%{release}
Provides:       %{lc_name}-devel%{?_isa} = %{version}-%{release}

%description devel
This package contains the development headers and library
for %{name}.

%package doc
Summary:        Documentation files for %{name}
Provides:       %{lc_name}-doc           = %{version}-%{release}

BuildArch:      noarch

%description doc
This package contains the documentation files and some brief examples
for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1
autoreconf -fiv

# Preserve examples.
cp -pr SampleDrivers examples
find examples -depth -name '.git*' -print0 | xargs -0 rm -f

%build
%configure			\
	--enable-examples	\
	--enable-openmp		\
	--disable-silent-rules	\
	--disable-static
%make_build

%install
%make_install

# We don't want those libtool dumplings and static libs.
find %{buildroot} -depth -name '*.*a' -print0 | xargs -0 rm -f

# Move the cli-tool to %%{_bindir}
mkdir -p %{buildroot}%{_bindir}
mv -f .libs/%{name} %{buildroot}%{_bindir}

# Kill rpath from binaries.
chrpath --delete %{buildroot}%{_bindir}/%{name}

# Remove build examples.
rm -rf %{buildroot}%{_prefix}/examples

# Install documentation.
mkdir -p %{buildroot}%{_pkgdocdir}
cp -pr AUTHORS ChangeLog README.md examples %{buildroot}%{_pkgdocdir}

%check
%make_build check

%ldconfig_scriptlets

%files
%doc %dir %{_pkgdocdir}
%license COPYING*
%doc %{_pkgdocdir}/README.md
%{_libdir}/lib%{name}.so.*

%files cli
%{_bindir}/%{name}

%files devel
%doc %{_pkgdocdir}/ChangeLog
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so

%files doc
%license %{_datadir}/licenses/%{name}*
%doc %{_pkgdocdir}

%changelog
%autochangelog
