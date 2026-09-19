%global source0_hash c789f6b13cc04cc97efd987323dcdcb87de2a7273f951b9c9e5558947fbda09f

Name:           hot-tux
Version:        0.3.1
Release:        23%{?dist}
Summary:        Graphical CPU utilization monitoring utility

# Automatically converted from old format: Artistic clarified - review is highly recommended.
License:        ClArtistic
URL:            https://github.com/judovana/hot-tux
Source0:        https://github.com/judovana/hot-tux/archive/%{name}-%{version}.tar.gz
Patch1:         makefile.patch

BuildRequires:  gcc
BuildRequires:  sed
BuildRequires:  coreutils
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gdk-2.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires: make

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{name}-%{version}
# Drop docfiles manipulation (installation)
sed -i -e "/DOC/d" Makefile

%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{__global_ldflags}"
%make_build PREFIX=%{_prefix}

%install
%make_install PREFIX=%{_prefix}

%files
%license LICENSE copyright
%doc NEWS config.example CONTRIBUTORS
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
