%global source0_hash 1456473841fb477372723472449f53caafe5b8ad4f23f14b644da77f7f7e313c

Name:           cinfo
Version:        0.5.10
Release:        5%{?dist}
Summary:        Fast and minimal system information tool

License:        GPL-3.0-only
URL:            https://github.com/mrdotx/cinfo
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make

%description
%{summary}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
# remove lines that build for pacman
sed -i -e '/\*PKGS_CMD/d' -e '/\*PKGS_DESC/d' config.def.h
# add lines to build for dnf
cat >> config.def.h << EOL
static const char *PKGS_CMD             = "rpm -qa | wc -l",
                  *PKGS_DESC            = " [dnf]";
EOL

%set_build_flags
%make_build

%install
%make_install PREFIX=%{_prefix}

%files
%license LICENSE.md
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
