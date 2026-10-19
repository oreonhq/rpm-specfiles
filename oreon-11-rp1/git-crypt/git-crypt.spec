%global source0_hash 540d424f87bed7994a4551a8c24b16e50d3248a5b7c3fd8ceffe94bfd4af0ad9
Name:       git-crypt
Version:    0.8.0
Release:        1%{?dist}
Summary:        Transparent file encryption in git
License:    GPL-3.0-or-later AND X11
URL:        https://www.agwa.name/projects/git-crypt
Source0:        https://www.agwa.name/projects/%{name}/downloads/%{name}-%{version}.tar.gz
Requires:       git
# oreon:deps
BuildRequires:  docbook-style-xsl
BuildRequires:  gcc-c++
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  openssl-devel
# /oreon:deps
%description
git-crypt enables transparent encryption and decryption of files in a
git repository. Files which you choose to protect are encrypted when
committed, and decrypted when checked out. git-crypt lets you freely
share a repository containing a mix of public and private
content. git-crypt gracefully degrades, so developers without the
secret key can still clone and commit to a repository with encrypted
files. This lets you store your secret material (such as keys or
passwords) in the same repository as your code, without requiring you
to lock down your entire repository.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
sed -i "s|^\tinstall -|\t\$(INSTALL) -|" Makefile

%build

export DOCBOOK_XSL=%{_datadir}/sgml/docbook/xsl-stylesheets/manpages/docbook.xsl
export ENABLE_MAN=yes
export CXXFLAGS="%{optflags} -DOPENSSL_API_COMPAT=0x30000000L"
export LDFLAGS="%{__global_ldflags}"
%make_build
%install
%make_install ENABLE_MAN=yes PREFIX=%{_prefix}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
