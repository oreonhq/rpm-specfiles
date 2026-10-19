%global source0_hash bf15251cb249a6028fd8532d31388b296dffc28c90782fcc0e7ba6f56354f4c5
%global modname lib%{name}
Name:           mat2
Version:        0.14.0
Release:        1%{?dist}
Summary:        Metadata removal tool, supporting a wide range of commonly used file formats
License:        LGPL-3.0-or-later
URL:            https://github.com/jvoisin/mat2
VCS:            git:%{url}.git
Source0:        https://github.com/jvoisin/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{url}/releases/download/%{version}/%{version}.tar.gz.asc
Source2:        gpgkey-9FCDEE9E1A381F311EA62A7404D041E8171901CC.gpg
Patch0:          %{name}-skip-broken-tests.patch
Patch1:          %{name}-py315-fix.patch
BuildArch:      noarch
Requires:       python3-%{modname} = %{version}-%{release}
Suggests:       %{name}-dolphin = %{version}-%{release}
%py_provides python3-%{name}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-mat2 = %{version}-%{release}
# /oreon:deps
%description

# Library package
%package     -n python3-%{modname}
Summary:        Library for %{name}
Requires:       gdk-pixbuf2
Requires:       librsvg2
Requires:       mailcap
Requires:       poppler-glib
Recommends:     %{_bindir}/ffmpeg
Recommends:     perl-Image-ExifTool
Recommends:     %{name} = %{version}-%{release}
%description -n python3-%{modname}

Library for %{name}.

# Dolphin package
%package        dolphin
Summary:        Dolphin integration for %{name}
Requires:       dolphin
Requires:       hicolor-icon-theme
Requires:       kdialog
Requires:       kf5-filesystem
Requires:       python3-%{modname} = %{version}-%{release}
%description dolphin

Dolphin integration for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%install
%pyproject_install
chmod 0755 %{buildroot}%{python3_sitelib}/%{modname}/__init__.py
install -D -p dolphin/%{name}.desktop -t \
    %{buildroot}%{_datadir}/kservices5/
install -D -p -m 644 data/%{name}.svg -t \
    %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%build

%pyproject_wheel
%check

%{py3_test_envvars} %{python3} -m unittest discover
%files
%files -n python3-libmat2 -f %{oreon_filedir}/python3-libmat2.list
%files -n mat2-dolphin -f %{oreon_filedir}/mat2-dolphin.list

%changelog

%autochangelog
