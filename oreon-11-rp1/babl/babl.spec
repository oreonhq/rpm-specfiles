%global source0_hash e676507b421d414d49db8627415dc1eadbd787536baa7d6fe94a1f1971cbe73e
%global skip_checks_version 0.1.58
%ifarch ppc64 ppc64le
%global skip_checks %nil
%else
  %ifarch s390x
  %global skip_checks float-to-8bit
  %else
  %global skip_checks %nil
  %endif
%endif
%global develdocdir %{_docdir}/%{name}-devel-%{version}/html
Summary:        A dynamic, any to any, pixel format conversion library
Name:       babl
Version:    0.1.128
Release:        1%{?dist}
%global plain_version %{lua:
    local plain_version = (string.gsub(macros.version, '^(.*)[%^~].*$', '%1'))
    print(plain_version)
    if plain_version ~= macros.version then
        macros.snapshot = (string.gsub(macros.version, '^.*[%^~](.*)$', '%1'))
        macros.git_rev = (string.gsub(macros.snapshot, '^.*git(.*)$', '%1'))
    end
}
%global major %{lua:
    print((string.gsub(macros.plain_version, '^(%d+)%..*$', '%1')))
}
%global minor %{lua:
    print((string.gsub(macros.plain_version, '^%d+%.(%d+)%..*$', '%1')))
}
%global micro %{lua:
    print((string.gsub(macros.plain_version, '^%d+%.%d+%.(%d+).*$', '%1')))
}
%global apiver %major.%minor
License:    LGPL-3.0-or-later AND GPL-3.0-or-later
URL:        https://www.gegl.org/babl/
Source0:        https://download.gimp.org/pub/%{name}/0.1/%{name}-%{version}.tar.xz
%if %defined git_rev
Patch:      babl-%{plain_version}-git%{git_rev}.patch
%endif
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gi-docgen
BuildRequires:  gobject-introspection-devel
BuildRequires:  librsvg2-tools
BuildRequires:  meson
BuildRequires:  openssh-clients
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  vala
# /oreon:deps
%description
Babl is a dynamic, any to any, pixel format conversion library. It
provides conversions between the myriad of buffer types images can be
stored in. Babl doesn't only help with existing pixel formats, but also
facilitates creation of new and uncommon ones.

%package devel
Summary:    Headers for developing programs that will use %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   pkgconfig
%description devel
This package contains the libraries and header files needed for
developing with %{name}.

%package devel-docs
Summary:    Documentation for developing programs that will use %{name}
BuildArch:  noarch
Requires:   %{name}-devel = %{version}-%{release}
Obsoletes:  %{name}-devel < 0.1.2-2%{?dist}
Conflicts:  %{name}-devel < 0.1.2-2%{?dist}
%description devel-docs
This package contains documentation needed for developing with %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n babl-%{plain_version}

%build

%meson
%meson_build
%install
%meson_install
mkdir -p "%{buildroot}/%{develdocdir}"
cp -pr "%{_vpath_builddir}"/docs/* "%{buildroot}/%{develdocdir}"
rm -f "%{buildroot}/%{develdocdir}/index.html.tmp"
mv "%{buildroot}/%{_docdir}/%{name}-%{apiver}" "%{buildroot}/%{develdocdir}"
%oreon_autofiles babl-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles babl-devel-docs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if "%version" == "%skip_checks_version"
pushd tests
for problematic in %skip_checks; do
    rm -f "$problematic"
    cat << EOF > "$problematic"
echo Skipping test "$problematic"
EOF
    chmod +x "$problematic"
done
popd
%endif
%meson_test
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n babl-devel -f %{oreon_filedir}/babl-devel.list
%files -n babl-devel-docs -f %{oreon_filedir}/babl-devel-docs.list

%changelog

%autochangelog
