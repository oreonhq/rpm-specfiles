#global candidate rc1

Name:    tpm2-tools
Version: 5.7
Release: 5%{?candidate:.%{candidate}}%{?dist}
Summary: A bunch of TPM testing toolS build upon tpm2-tss

License: BSD-3-Clause
URL:     https://github.com/tpm2-software/tpm2-tools
Source0: https://github.com/tpm2-software/tpm2-tools/releases/download/%{version}%{?candidate:-%{candidate}}/%{name}-%{version}%{?candidate:-%{candidate}}.tar.gz

BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: libtool
BuildRequires: autoconf-archive
%if ! 0%{?rhel}
BuildRequires: pandoc
%endif
BuildRequires: pkgconfig(cmocka)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(openssl)
# tpm2-tss-devel provides tss2-mu/sys/esys package config
BuildRequires: pkgconfig(tss2-mu) >= 3.1.0
BuildRequires: pkgconfig(tss2-sys) >= 3.1.0
BuildRequires: pkgconfig(tss2-esys) >= 3.1.0
BuildRequires: pkgconfig(uuid)

# tpm2-tools is heavily depending on TPM2.0-TSS project, matched tss is required
Requires: tpm2-tss%{?_isa} >= 3.1.0

%description
tpm2-tools is a batch of tools for tpm2.0. It is based on tpm2-tss.

%prep
%autosetup -p1 -n %{name}-%{version}%{?candidate:-%{candidate}}

%build
%configure --prefix=/usr --disable-static --disable-silent-rules
%make_build

%install
%make_install

%files
%license docs/LICENSE
%doc docs/README.md docs/CHANGELOG.md
%{_bindir}/tpm2
%{_bindir}/tpm2_*
%{_bindir}/tss2
%{_bindir}/tss2_*
%{_datadir}/bash-completion/completions/tpm2*
%{_datadir}/bash-completion/completions/tss2*
%{_mandir}/man1/tpm2_*.1.gz
%{_mandir}/man1/tpm2.1.gz
%{_mandir}/man1/tss2_*.1.gz

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.7-5
- Prepare for Oreon 11 (RP1)
