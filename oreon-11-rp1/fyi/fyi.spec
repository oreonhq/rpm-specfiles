%global source0_hash 6d196b4725df02dba39ca736c0f5b485f6a204a98f68de6bbe8155bdc1e56d24

Name:           fyi
Version:        1.0.4
Release:        %autorelease
Summary:        Command line utility to send desktop notifications
License:        MIT
URL:            https://codeberg.org/dnkl/fyi
Source:         https://codeberg.org/dnkl/%{name}/archive/%{version}.tar.gz

Patch0:		fyi-no-const.patch

BuildRequires:  dbus-devel
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  scdoc

%description
FYI (for your information) is a command line utility to send desktop
notifications to the user via a notification daemon implementing XDG desktop
notifications.

%package bash-completion
Summary: Bash completion files for %{name}
Requires: bash-completion
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description bash-completion
%{summary}

%package fish-completion
Summary: Fish completion files for %{name}
Requires: fish
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description fish-completion
%{summary}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}

%build
%meson
%meson_build

%install
%meson_install
rm -r %{buildroot}/%{_datadir}/doc/%{name}/

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz

%files bash-completion
%{_datadir}/bash-completion/completions/%{name}

%files fish-completion
%{_datadir}/fish/vendor_completions.d/%{name}.fish

%changelog
%autochangelog
