%global source0_hash 459e941fe5833f482e8ec50ed6ba886a07128a171ee0a12da762317e68dc142d
Name:           cinfo
Version:        0.5.12
Release:        1%{?dist}
Summary:        Fast and minimal system information tool
License:        GPL-3.0-only
URL:            https://github.com/mrdotx/cinfo
Source0:        https://github.com/mrdotx/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
%{summary}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

sed -i -e '/\*PKGS_CMD/d' -e '/\*PKGS_DESC/d' config.def.h
cat >> config.def.h << EOL
static const char *PKGS_CMD             = "rpm -qa | wc -l",
                  *PKGS_DESC            = " [dnf]";
EOL
%set_build_flags
%make_build
%install
%make_install PREFIX=%{_prefix}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
