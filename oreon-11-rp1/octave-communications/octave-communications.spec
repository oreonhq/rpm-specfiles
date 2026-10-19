%global source0_hash 5176a8578e6676603b9f6701f09dd2fbff0db7bba1a24cafd8c5419be14ae65c
%global octpkg communications
Name:           octave-%{octpkg}
Version:        1.2.7
Release:        1%{?dist}
Summary:        Communications for Octave
License:        GPL-3.0-or-later
URL:            https://gnu-octave.github.io/packages/communications/
Source0:        https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
Source1:        mkdoc
Source2:        mktexi
ExcludeArch:    aarch64
Requires:       octave(api) = %{octave_api}
Requires:       octave-signal >= 1.0.0 
Requires:       octave-image >= 0.0.0
Requires(post): octave
Requires(postun): octave
Obsoletes:      octave-forge <= 20090607
ExcludeArch:    s390x
# oreon:deps
BuildRequires:  automake
BuildRequires:  hdf5-devel
BuildRequires:  make
BuildRequires:  octave-devel
BuildRequires:  octave-image
BuildRequires:  octave-signal
BuildRequires:  texinfo-tex
# /oreon:deps
%description
Digital Communications, Error Correcting Codes (Channel Code), Source Code
functions, Modulation and Galois Fields

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{octpkg}-%{version}
cp -p %{SOURCE1} %{SOURCE2} .
chmod a+x mkdoc mktexi
cd src
autoreconf
cd -
make -C doc comms.texi

%build

export MKOCTFILE="mkoctfile -v"
%octave_pkg_build
make -C doc
%install
%octave_pkg_install
rm -rf %{buildroot}/%{octpkgdir}/doc
install -m 0644 doc/comms.info %{buildroot}/%{octpkgdir}
chmod a-x %{buildroot}/%{octpkgdir}/*.m
chmod a-x %{buildroot}/%{octpkgdir}/@galois/*.m
%oreon_autofiles main

%post

%octave_cmd pkg rebuild
%preun

%octave_pkg_preun
%postun

%octave_cmd pkg rebuild
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
