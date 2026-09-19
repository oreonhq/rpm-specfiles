%global source0_hash 831db9f31d2da31adfc264460da94daee494c4b9db9c2c0db5f406792abb2077

%global commit0 f31c39cc2eadd0ab7f29f34becba1348ae9f8721
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global snapdate 20250707

%global __python %{__python3}

Name:           icestorm
Version:        0
Release:        0.43.%{snapdate}git%{shortcommit0}%{?dist}
Summary:        Lattice iCE40 FPGA bitstream creation/analysis/programming tools
License:        ISC
URL:            http://bygone.clairexen.net/%{name}
Source0:        https://github.com/YosysHQ/%{name}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz

# Fedora-specific patch for datadir
Patch1:         %{name}-datadir.patch

BuildRequires:  gcc-c++
BuildRequires:  python%{python3_pkgversion} libftdi-devel
BuildRequires:  make

%description
Project IceStorm aims at documenting the bitstream format of Lattice iCE40
FPGAs and providing simple tools for analyzing and creating bitstream files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{commit0}
%patch 1 -p1 -b .datadir

# fix shebang lines in Python scripts
find . -name \*.py -exec sed -i 's|/usr/bin/env python3|/usr/bin/python3|' {} \;
# get rid of .gitignore files in examples
find . -name \.gitignore -delete

%build
%global moreflags -I/usr/include/libftdi1
make %{?_smp_mflags} \
     CFLAGS="%{optflags} %{moreflags}" \
     CXXFLAGS="%{optflags} %{moreflags}" \
     PREFIX="%{_prefix}" \
     CHIPDB_SUBDIR="%{name}" \
     LDFLAGS="$RPM_LD_FLAGS"

%install
%make_install PREFIX="%{_prefix}"
chmod +x %{buildroot}%{_bindir}/icebox.py
mv %{buildroot}%{_datarootdir}/icebox %{buildroot}%{_datarootdir}/%{name}
install -pm644 icefuzz/timings_*.txt %{buildroot}%{_datarootdir}/%{name}

# We could do a minimal check section by running make in the example
# directories, but that depends on arachne-pnr, which depends on this
# package, so it would create a circular dependency.

%files
%license README
%doc examples
%{_bindir}/*
%{_datarootdir}/%{name}

%changelog
%autochangelog
