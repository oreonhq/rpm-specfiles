%global source0_hash 7ad75e0d1b29087335fbb1691b05a800f777f4ec9cba84faa19355075d7f0f89

Name:           ranger
Version:        1.9.4
Release:        9%{?dist}
Summary:        A vim-like file manager
License:        GPL-3.0-only
URL:            https://ranger.github.io/
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  desktop-file-utils
BuildRequires:  python3-devel
#Suggests:       w3m-img

%description
Ranger is a free console file manager that gives you greater flexibility and a
good overview of your files without having to leave your *nix console. It
visualizes the directory tree in two dimensions: the directory hierarchy on
one, lists of files on the other, with a preview to the right so you know where
you'll be going.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
sed -i -e '1d;2i#!/usr/bin/python3' %{name}.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l '*'
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
mv %{buildroot}%{_pkgdocdir} _doc
find _doc -type f -exec chmod -R -x '{}' \;

%check
%pyproject_check_import

%files -f %{pyproject_files}
%doc _doc/*
%{_bindir}/ranger
%{_bindir}/rifle
%{_datadir}/applications/ranger.desktop
%{_mandir}/man1/ranger.1*
%{_mandir}/man1/rifle.1*

%changelog
%autochangelog
