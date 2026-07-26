%global source0_hash 3c1821de3c2dcb06fb975c8e3e28506b3987af952d3d75facdfda1e5e9160189

%global		pkg		apel
%global		pkgname		APEL
%global		ver	10.8
%global		snap	82eb232
%global		snapver	^1.git%{snap}

Name:		emacs-%{pkg}
Version:	%{ver}%{?snapver}
Release:	0.7%{?dist}
Summary:	A Portable Emacs Library

License:	GPL-2.0-or-later
URL:		https://github.com/wanderlust/apel/tree/apel-wl
# No releases
Source0:	%{pkg}-%{ver}-%{snap}.tar.gz

BuildArch:	noarch
BuildRequires:	emacs
BuildRequires: make
Requires:	emacs(bin) >= %{_emacs_version}
Provides:	apel = %{version}-%{release}
Obsoletes:	apel < 10.8-1
Provides:	emacs-apel-el <= 10.8-8
Obsoletes:	emacs-apel-el <= 10.8-8

Patch0:		APEL-CFG.patch
Patch1:		apel-10.4-missing-el.patch

%description
%{pkgname} (A Portable Emacs Library) is a library to support
to write portable Emacs Lisp programs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pkg}-%{ver}-%{snap} -p1

%build

%install
make PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	LISPDIR=$RPM_BUILD_ROOT%{_emacs_sitelispdir} \
	INSTALL="install -p"  install

%files
%doc README.en ChangeLog.1
%lang(ja) %doc README.ja
%{_emacs_sitelispdir}/%{pkg}/*.el
%{_emacs_sitelispdir}/%{pkg}/*.elc
%dir %{_emacs_sitelispdir}/%{pkg}

%changelog
%autochangelog
