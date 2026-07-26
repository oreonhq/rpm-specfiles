%global source0_hash b8aa9e4b158d5c4a098b18d109c0f8c596e73118c102d6f00789f9149feb8579

Name:           katarakt
Version:        0.3
Release:        %autorelease
Summary:        Simple PDF viewer

%global forgeurl https://gitlab.cs.fau.de/Qui_Sum/%{name}
%global tag      v%{version}
%forgemeta

License:        BSD-2-Clause
URL:            %{forgeurl}
Source0:        %{forgesource}
Source1:        %{name}.desktop
Source2:        de.fau.cs.gitlab.%{name}.metainfo.xml

BuildRequires:  asciidoc
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  poppler-qt6-devel
BuildRequires:  qt6-qtbase-devel

%description
katarakt is a simple PDF viewer.
It is designed to use as much available screen space as possible.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n "%{name}-%{tag}"

%build
%qmake_qt6
%make_build
a2x -f manpage doc/katarakt.txt

%install
# The qmake `install` target does nothing; install the relevant files manually
install -D -m 755 -p -t "%{buildroot}%{_bindir}"             "%{name}"
install -D -m 644 -p -t "%{buildroot}%{_mandir}/man1"        "doc/%{name}.1"
install -D -m 644 -p -t "%{buildroot}%{_sysconfdir}/xdg"     "share/%{name}.ini"
install -D -m 644 -p -t "%{buildroot}%{zsh_completions_dir}" "completion/_%{name}"

desktop-file-install "%{SOURCE1}"
install -D -m 644 -p -t "%{buildroot}%{_metainfodir}" "%{SOURCE2}"

%check
appstream-util validate-relax --nonet \
  "%{buildroot}%{_metainfodir}"/*.metainfo.xml

%files
%config(noreplace) %{_sysconfdir}/xdg/%{name}.ini
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1*
%{_metainfodir}/de.fau.cs.gitlab.%{name}.metainfo.xml
%{zsh_completions_dir}/_%{name}

%changelog
%autochangelog
