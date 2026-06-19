%global source0_hash f47259bc38ba553b0deb8b6dab6b5b73d3630469a7c9439ccdca80e06d7c1ece

%global maj 0

Name:           serd
Version:        0.32.8
Release:        %autorelease
Summary:        A lightweight C library for RDF syntax

License:        ISC
URL:            https://drobilla.net/software/%{name}.html
Source0:        https://download.drobilla.net/%{name}-%{version}.tar.xz
Source1:        https://download.drobilla.net/%{name}-%{version}.tar.xz.sig
Source2:        https://drobilla.net/drobilla.gpg

BuildRequires:  meson
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  python3
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_lv2_theme
BuildRequires:  python-sphinxygen

%description
%{name} is a lightweight C library for RDF syntax which supports reading and 
writing Turtle, TRiG, NTriples, and NQuads.

Serd is suitable for performance-critical or resource-limited applications,
such as serialising very large data sets, network protocols, or embedded
systems that require minimal dependencies and lightweight deployment.

%package devel
Summary:        Development libraries and headers for %{name}
Requires:       %{name}%{_isa} = %{version}-%{release}

%description devel
%{name} is a lightweight C library for RDF syntax which supports reading and 
writing Turtle, TRiG, NTriples, and NQuads.

This package contains the headers and development libraries for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%meson -Dman_html=disabled
%meson_build

%install
%meson_install
# Move devel docs to the right directory
install -d %{buildroot}%{_docdir}/%{name}
mv %{buildroot}%{_docdir}/%{name}-%{maj} %{buildroot}%{_docdir}/%{name}

%check
%meson_test

%files
%license COPYING
%doc AUTHORS NEWS README.md
%doc %{_mandir}/man1/serdi.1*
%{_libdir}/lib%{name}-%{maj}.so.%{maj}*
%{_bindir}/serdi

%files devel
%doc %{_docdir}/%{name}/%{name}-%{maj}/
%{_libdir}/lib%{name}-%{maj}*.so
%{_libdir}/pkgconfig/%{name}*.pc
%{_includedir}/%{name}-%{maj}/

%changelog
%autochangelog
