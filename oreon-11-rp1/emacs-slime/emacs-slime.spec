%global source0_hash 530f0780e62b517cb60f519416e08a7a5d46b370a2b0cf718f39e0cb580ce382
%global pkg slime
Name:            emacs-%{pkg}
Epoch:           2
Version:         2.32
Release:        1%{?dist}
Summary:        The superior lisp interaction mode for emacs
License:         LicenseRef-Fedora-Public-Domain AND GPL-3.0-or-later AND GPL-2.0-or-later AND LLGPL
URL:             http://common-lisp.net/project/slime/
Source0:        https://github.com/%{pkg}/%{pkg}/archive/v%{version}.tar.gz#/%{pkg}-%{version}.tar.gz
Requires:        emacs(bin) >= %{_emacs_version} common-lisp-controller
Requires(post):  common-lisp-controller
Requires(preun): common-lisp-controller
Provides:        %{name}-el = %{epoch}:%{version}-%{release}
Obsoletes:       %{name}-el < 1:2.19-5
BuildArch:      noarch
ExclusiveArch:  %{arm} %{ix86} x86_64 ppc sparcv9 aarch64
# oreon:deps
BuildRequires:  common-lisp-controller
BuildRequires:  emacs
BuildRequires:  make
BuildRequires:  sbcl
BuildRequires:  texinfo
# /oreon:deps
%description
SLIME is a Emacs mode for common Lisp development.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pkg}-%{version} -p1

%build

make
cd doc/
make slime.info
%install
install -pm 755 -d %{buildroot}%{_emacs_sitestartdir}
install -pm 644 *.el  %{buildroot}%{_emacs_sitestartdir}
install -pm 755 -d %{buildroot}%{_infodir}
install -pm 644 doc/%{pkg}.info %{buildroot}%{_infodir}/
install -pm 755 -d %{buildroot}%{_emacs_sitelispdir}/%{pkg}
install -pm 755 -d %{buildroot}%{_emacs_sitelispdir}/%{pkg}/contrib
install -pm 755 -d %{buildroot}%{_emacs_sitelispdir}/%{pkg}/lib
install -pm 644 *.el* %{buildroot}%{_emacs_sitelispdir}/%{pkg}/
install -pm 644 lib/*.el* %{buildroot}%{_emacs_sitelispdir}/%{pkg}/lib/
install -pm 755 -d %{buildroot}%{_datadir}/common-lisp/source/slime
install -pm 755 -d %{buildroot}%{_datadir}/common-lisp/source/slime/contrib
install -pm 755 -d %{buildroot}%{_datadir}/common-lisp/source/slime/lib
install -pm 755 -d %{buildroot}%{_datadir}/common-lisp/source/slime/swank
install -pm 644 *.lisp %{buildroot}%{_datadir}/common-lisp/source/slime
install -pm 644 contrib/*.lisp %{buildroot}%{_datadir}/common-lisp/source/slime/contrib
install -pm 644 contrib/*.el %{buildroot}%{_datadir}/common-lisp/source/slime/contrib
install -pm 644 contrib/README.md %{buildroot}%{_datadir}/common-lisp/source/slime/contrib
install -pm 644 lib/*.el %{buildroot}%{_datadir}/common-lisp/source/slime/lib
install -pm 644 swank/*.lisp %{buildroot}%{_datadir}/common-lisp/source/slime/swank
install -pm 644 *.asd %{buildroot}%{_datadir}/common-lisp/source/slime
mv contrib/README.md contrib/contrib-README.md
%oreon_autofiles main

%check

make check
%post

/usr/sbin/register-common-lisp-source swank
%preun

/usr/sbin/unregister-common-lisp-source swank 
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
