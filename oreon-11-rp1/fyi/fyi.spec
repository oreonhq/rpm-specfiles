%global source0_hash 584fc3966a21949dbcc655d8693497384dade382d332be1cf92eae958336a145
Name:           fyi
Version:        1.0.4
Release:        1%{?dist}
Summary:        Command line utility to send desktop notifications
License:        MIT
URL:            https://codeberg.org/dnkl/fyi
Source0:        https://codeberg.org/dnkl/%{name}/archive/%{version}.tar.gz
Patch0:		fyi-no-const.patch
# oreon:deps
BuildRequires:  dbus-devel
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  scdoc
# /oreon:deps
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
%global oreon_srcdir %{name}
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
rm -r %{buildroot}/%{_datadir}/doc/%{name}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n fyi-bash-completion -f %{oreon_filedir}/fyi-bash-completion.list
%files -n fyi-fish-completion -f %{oreon_filedir}/fyi-fish-completion.list

%changelog

%autochangelog
