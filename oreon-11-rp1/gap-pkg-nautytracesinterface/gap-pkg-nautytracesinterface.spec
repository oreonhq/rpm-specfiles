%global source0_hash c7ed3f147e5fd5e1f9c7fdb41f7df5f5d06438cb738829f3a2c49d4be6c59e8d
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond bootstrap 0
%global date           20251125
%global commit         530c14844dc789d6c6af026758451482c4bfc684
%global user           gap-packages
%global gap_pkgname    nautytracesinterface
%global gap_skip_check %{?with_bootstrap}
%global forgeurl       https://github.com/gap-packages/NautyTracesInterface
Name:           gap-pkg-%{gap_pkgname}
Version:        0.3
Summary:        GAP interface to nauty and Traces
%forgemeta
Release:        1%{?dist}
License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/NautyTracesInterface/
VCS:            git:%{forgeurl}.git
Source0:        %{forgeurl}/archive/%{commit}/NautyTracesInterface-%{commit}.tar.gz
Patch:          %{name}-nauty.patch
ExcludeArch:    %{ix86}
BuildSystem:    gap
BuildOption(install): bin examples gap tst
BuildOption(check): tst/testall.g
%if %{without bootstrap}
%endif
Requires:       gap-core%{?_isa}
# oreon:deps
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-digraphs
BuildRequires:  gap-pkg-grape
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(libnauty)
# /oreon:deps
%description
This GAP package provides an interface to nauty and Traces.

%package doc
License:        GPL-2.0-or-later AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        NautyTracesInterface documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%conf
# Make sure the bundled nauty is not used
rm -fr nauty*

# Generate the configure script
autoreconf -fi

%build

%configure --with-gaproot=%{gap_archdir} --with-nauty=%{_includedir}/nauty \
  --disable-silent-rules
%make_build
%make_build doc
%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-nautytracesinterface-doc -f %{oreon_filedir}/gap-pkg-nautytracesinterface-doc.list

%changelog

%autochangelog
