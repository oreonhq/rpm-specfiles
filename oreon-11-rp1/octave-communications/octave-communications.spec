%global source0_hash 5176a8578e6676603b9f6701f09dd2fbff0db7bba1a24cafd8c5419be14ae65c

%global octpkg communications

Name:           octave-%{octpkg}
Version:        1.2.7
Release:        4%{?dist}
Summary:        Communications for Octave
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://gnu-octave.github.io/packages/communications/
Source0:        https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
# the following are required to build the documentation, and they come from the main octave package
Source1:        mkdoc
Source2:        mktexi

# currently no octave-signal due to no octave-control on aarch64
ExcludeArch:    aarch64

BuildRequires: make
BuildRequires:  octave-devel
BuildRequires:  octave-signal >= 1.0.0
BuildRequires:  octave-image >= 0.0.0
BuildRequires:  hdf5-devel
BuildRequires:  texinfo-tex
# For patches that requires autoreconf
BuildRequires:  automake

Requires:       octave(api) = %{octave_api}
Requires:       octave-signal >= 1.0.0 
Requires:       octave-image >= 0.0.0
Requires(post): octave
Requires(postun): octave

Obsoletes:      octave-forge <= 20090607

# octave-signal not available for s390x
ExcludeArch:    s390x

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
# remove doc build junk
rm -rf %{buildroot}/%{octpkgdir}/doc
install -m 0644 doc/comms.info %{buildroot}/%{octpkgdir}
chmod a-x %{buildroot}/%{octpkgdir}/*.m
chmod a-x %{buildroot}/%{octpkgdir}/@galois/*.m

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%{octpkglibdir}

%dir %{octpkgdir}
%doc %{octpkgdir}/doc-cache
%{octpkgdir}/*.m
%{octpkgdir}/@galois/*.m
%{octpkgdir}/packinfo
%{octpkgdir}/comms.info

%changelog
%autochangelog
