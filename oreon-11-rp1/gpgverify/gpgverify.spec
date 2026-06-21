Name:           gpgverify
Version:        2.2
Release:        4%{?dist}
Summary:        Signature verifier for easy and safe scripting

License:        Boehm-GC
URL:            https://src.fedoraproject.org/rpms/gpgverify
Source0:        gpgverify
Source1:        macros.gpgverify
Source2:        license.txt
BuildArch:      noarch

Requires:       grep gnupg2 gnupg2-verify

%description
GPGverify is a wrapper around GnuPG's gpgv. It verifies a file against an
OpenPGP signature and one or more keyrings.

%prep
%setup -c -T
cp --preserve=timestamps %{sources} .

%install
mkdir --parents %{buildroot}%{_libexecdir}
cp --preserve=timestamps gpgverify %{buildroot}%{_libexecdir}/

%files
%attr(0755,-,-) %{_libexecdir}/gpgverify
%license license.txt

%changelog
%autochangelog
