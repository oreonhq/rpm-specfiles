%global source0_hash 307f9086e0b063d439dc4f513e36a145e8a57f23de448aefae2a6c00f6da6fd2
%global pkg_name pretty-show
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%bcond system_jquery 0
Name:           ghc-%{pkg_name}
Version:        1.10
Release:        1%{?dist}
Summary:        Tools for working with derived Show instances and generic inspection of values
License:        MIT
URL:            https://hackage.haskell.org/package/pretty-show
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
%if %{with system_jquery}
Requires:       js-jquery
%else
Provides:       bundled(jquery) = 3.3.1
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-array-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-haskell-lexer-devel
BuildRequires:  ghc-haskell-lexer-prof
BuildRequires:  ghc-pretty-devel
BuildRequires:  ghc-pretty-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  happy
# /oreon:deps
%description
We provide a library and an executable for working with derived 'Show'
instances. By using the library, we can parse derived 'Show' instances into a
generic data structure. The 'ppsh' tool uses the library to produce
human-readable versions of 'Show' instances, which can be quite handy for
debugging Haskell programs. We can also render complex generic values into an
interactive Html page, for easier examination.

%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
This package provides the Haskell %{pkg_name} library development files.

%if %{with haddock}
%package doc
Summary:        Haskell %{pkg_name} library documentation
BuildArch:      noarch
Requires:       ghc-filesystem
%description doc
This package provides the Haskell %{pkg_name} library documentation.
%endif

%if %{with ghc_prof}
%package prof
Summary:        Haskell %{pkg_name} profiling library
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Supplements:    (%{name}-devel and ghc-prof)
%description prof
This package provides the Haskell %{pkg_name} profiling library.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Begin cabal-rpm setup:
%setup -q -n %{pkgver}
# End cabal-rpm setup

%build

%ghc_lib_build
%install
%ghc_lib_install
%if %{with system_jquery}
%global _style_dir %{buildroot}%{_datadir}/%{pkgver}/style
rm -v %{_style_dir}/jquery.js
ln -s %{_webassetdir}/jquery/1/jquery.min.js %{_style_dir}/jquery.js
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%files -f %{oreon_filedir}/main.list
%files -n ghc-pretty-show-devel -f %{oreon_filedir}/ghc-pretty-show-devel.list
%files -n ghc-pretty-show-doc -f %{oreon_filedir}/ghc-pretty-show-doc.list
%files -n ghc-pretty-show-prof -f %{oreon_filedir}/ghc-pretty-show-prof.list

%changelog

%autochangelog
