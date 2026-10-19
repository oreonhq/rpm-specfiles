%global source0_hash d92c5214ea75b8a70214d7d7f6824207fc53861ec923ceb2cc574f2ec9effa94
Name: sextractor
Version: 2.28.2
Release:        1%{?dist}
Summary:        Extract catalogs of sources from astronomical images
License: GPL-3.0-or-later
URL: http://astromatic.iap.fr/software/%{name}
Source0:        https://github.com/astromatic/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0: sextractor-format-sec.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cfitsio-devel
BuildRequires:  fftw-devel
BuildRequires:  flexiblas-devel
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
SExtractor is a program that builds a catalogue of objects from an 
astronomical image. Although it is particularly oriented towards 
reduction of large scale galaxy-survey data, it performs rather 
well on moderately crowded star fields.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
sh ./autogen.sh
sed -i 's/openblas/flexiblas/g' configure

%build

%configure --enable-flexiblas --with-flexiblas-incdir=%{_includedir}/flexiblas
%make_build
%install
%make_install
mkdir -p %{buildroot}%{_datadir}/%{name}
install -m 644 -p config/*.conv %{buildroot}%{_datadir}/%{name}
install -m 644 -p config/default.nnw %{buildroot}%{_datadir}/%{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
