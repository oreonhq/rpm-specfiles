%global source0_hash dd2d7e6ce1ee9b78bc3a2d076f4c1b282b61e9a3a20456566d3e62d32dc12d5e

# RPM Spec file for redwax-tool

Name:          redwax-tool
Version:       1.0.0
Release:       %autorelease -b 1
ExcludeArch:   %{ix86}
Summary:       The redwax tool
License:       Apache-2.0
Source0:       https://archive.redwax.eu/dist/rt/%{name}-%{version}/%{name}-%{version}.tar.bz2
Source1:       https://archive.redwax.eu/dist/rt/%{name}-%{version}/%{name}-%{version}.tar.bz2.asc
Source2:       https://source.redwax.eu/svn/dist/rt/keys/KEYS
Source3:       redwax-test-certificates.pem
Url:           https://redwax.eu/rs/
BuildRequires: gnupg2
BuildRequires: gcc
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: pkgconfig(apr-1)
BuildRequires: pkgconfig(apr-util-1)
BuildRequires: pkgconfig(libcrypto)
BuildRequires: pkgconfig(nss)
BuildRequires: pkgconfig(p11-kit-1)
BuildRequires: pkgconfig(libical)
BuildRequires: pkgconfig(ldns)
BuildRequires: pkgconfig(libunbound)

%description
The redwax tool allows certificates and keys in a range of formats to
be read, searched for, and converted into other formats as needed by
common services.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q
%build
%configure --with-openssl --with-nss --with-p11-kit --with-libical --with-ldns --with-unbound --with-bash-completion-dir=%{bash_completions_dir}
%make_build

%install
%make_install

%check
./redwax-tool --pem-in '%{SOURCE3}' --filter-expiry=ignore --filter verify --metadata-out -

%files
%{_bindir}/redwax-tool
%{_mandir}/man1/redwax-tool.1*
%{bash_completions_dir}/redwax-tool

%doc AUTHORS ChangeLog README
%license COPYING

%changelog
%autochangelog
