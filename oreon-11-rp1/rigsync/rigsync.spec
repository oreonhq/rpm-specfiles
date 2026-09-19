%global source0_hash 5a1f859fbca03bfd429d0dc08492d8a6b47563288f91a6c0582774be7992c455

%global git_commit b320c4d9a3ced9529391ac969cc29ff63f1c523a
%global git_date 20230612

%global git_short_commit %(echo %{git_commit} | cut -c -8)
%global git_suffix %{git_date}git%{git_short_commit}

Name:		rigsync
Version:	0~%{git_suffix}
Release:	9%{?dist}
Summary:	Rigsync keeps multiple rigs frequency and mode in sync using Hamlib
License:	LGPL-2.1-only
URL:		https://github.com/daveriesz/%{name}
Source0:	%{url}/archive/%{git_commit}/%{name}-%{git_suffix}.tar.gz

ExcludeArch:    i686

BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	coreutils
BuildRequires:	hamlib-devel

%description
Rigsync is a utility that keeps the frequency and mode of multiple radios in
sync. Supported radios are all those supported by whatever version of
Hamlib to which rigsync is linked.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{git_commit}

%build
%make_build CFLAGS="%{build_cflags} -DDEBUG" LDFLAGS="%{build_ldflags} -lhamlib"

%install
install -Dp %{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/rigsync

%changelog
%autochangelog
