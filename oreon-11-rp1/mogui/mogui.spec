%global source0_hash 9b0b1a5aecff5db30e214d0e193cb2db6f35f89c672adf0267d00f9967512cc1

%global srcname modules-gui
Name:           mogui
Version:        0.2.2
Release:        11%{?dist}
Summary:        Graphical User Interface for Environment Modules

# icon files are licensed under CC-BY-SA-3.0 terms
License:        GPL-2.0-or-later AND CC-BY-SA-3.0
URL:            https://github.com/cea-hpc/mogui
Source:         %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
Requires:       environment-modules

%description
MoGui is a Graphical User Interface (GUI) for Environment Modules. It helps
users selecting modules to load and save module collections.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{name}

install -d %{buildroot}%{_datadir}/pixmaps
install -p -m 0644 mogui/icons/mogui-light/symbolic/apps/environment-modules.svg %{buildroot}%{_datadir}/pixmaps/%{name}.svg

install -d %{buildroot}%{_datadir}/applications
install -p -m 0644 share/%{name}.desktop %{buildroot}%{_datadir}/applications/

install -d %{buildroot}%{_metainfodir}
install -p -m 0644 share/%{name}.metainfo.xml %{buildroot}%{_metainfodir}/

install -d %{buildroot}%{_sysconfdir}/profile.d
install -d %{buildroot}%{_datadir}/fish/vendor_conf.d
install -p -m 0644 share/setup-env.sh %{buildroot}%{_sysconfdir}/profile.d/%{name}.sh
install -p -m 0644 share/setup-env.csh %{buildroot}%{_sysconfdir}/profile.d/%{name}.csh
install -p -m 0644 share/setup-env.fish %{buildroot}%{_datadir}/fish/vendor_conf.d/%{name}.fish

# "mogui" bin is not needed, as mogui shell function is defined at shell session start
# and desktop file relies on the "mogui-cmd" bin
rm %{buildroot}%{_bindir}/%{name}

%check
%pyproject_check_import
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.metainfo.xml

%files -f %{pyproject_files}
%doc ChangeLog README.md TODO.md
%{_bindir}/%{name}-cmd
%{_bindir}/%{name}-setup-env
%{_sysconfdir}/profile.d/%{name}.csh
%{_sysconfdir}/profile.d/%{name}.sh
%{_datadir}/fish/vendor_conf.d/%{name}.fish
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.svg
%{_metainfodir}/%{name}.metainfo.xml

%changelog
%autochangelog
