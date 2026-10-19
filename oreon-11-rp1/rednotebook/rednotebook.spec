%global source0_hash f0eddb338a74c5819000a6be16ef24b2821f9e60f86b3505f93f9a5bd2e3e9b2
Name: rednotebook
Version: 2.42
Release:        1%{?dist}
Summary:        Daily journal with calendar, templates and keyword searching
License: GPL-2.0-or-later
URL: https://rednotebook.app/
Source0:        https://github.com/jendrikseipp/rednotebook/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch: noarch
Requires: python3-PyYAML
Requires: webkit2gtk4.1
Requires: hicolor-icon-theme
Requires: gtksourceview4
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-rednotebook = %{version}-%{release}
# /oreon:deps
%description
RedNotebook is a modern desktop journal. It lets you format, tag and
search your entries. You can also add pictures, links and customizable
templates, spell check your notes, and export to plain text, HTML,
Latex or PDF.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
desktop-file-install                                    \
    --add-category="Calendar"                           \
    --delete-original                                   \
    --dir=%{buildroot}%{_datadir}/applications          \
    %{buildroot}/%{_datadir}/applications/%{name}.desktop
mkdir -p %{buildroot}/%{_datadir}/appdata/
mv %{buildroot}/%{_datadir}/metainfo/%{name}.appdata.xml %{buildroot}/%{_datadir}/appdata/
%find_lang %{name}
%oreon_autofiles main

%files

%changelog

%autochangelog
