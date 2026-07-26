%global source0_hash 21877e912a63c69253538dc8ba6ae3beb1c89f35222e8381d14320f6537cec89

Name:          mg
Version:       20260227
Release:       1%{?dist}
Summary:       Tiny Emacs-like editor
License:       LicenseRef-Fedora-Public-Domain
URL:           https://github.com/hboetes/mg
Source0:       https://github.com/hboetes/%{name}/archive/%{version}.tar.gz
BuildRequires: make
BuildRequires: gcc
BuildRequires: ncurses-devel
BuildRequires: libbsd-devel >= 0.7.0

%description
mg is a tiny public-domain Emacs-like editor included in the base OpenBSD
system. It is compatible with Emacs because there shouldn't be any reason to
learn more editor types than Emacs or vi.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%make_build CFLAGS="%{optflags}" LDFLAGS="%{optflags} -lncurses" libdir="%{_libdir}"

%install
rm -rf %{buildroot}
%make_install prefix=%{_prefix} mandir=%{_mandir}

%files
%doc README tutorial
%{_bindir}/mg
%{_mandir}/man1/mg.1.*

%changelog
%autochangelog
