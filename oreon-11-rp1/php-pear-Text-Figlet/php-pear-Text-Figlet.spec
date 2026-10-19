%global source0_hash 46bb1580fcf78c96465b2f60ebc855bb3a182f87cf09d097511820a64f17fb6b
%{!?pear_metadir: %global pear_metadir %{pear_phpdir}}
%{!?__pear: %{expand: %%global __pear %{_bindir}/pear}}
%global pear_name Text_Figlet
Name:           php-pear-Text-Figlet
Version:        1.0.2
Release:        1%{?dist}
Summary:        Render text using FIGlet fonts
License:        PHP-3.01
URL:            http://pear.php.net/package/Text_Figlet
Source0:        http://pear.php.net/get/%{pear_name}-%{version}.tgz
Source1:        LICENSE
BuildArch:      noarch
Requires(post): %{__pear}
Requires(postun): %{__pear}
Requires:       php-pcre
Requires:       php-zip
Requires:       php-pear(PEAR)
Provides:       php-pear(%{pear_name}) = %{version}
# oreon:deps
BuildRequires:  php-pear(PEAR)
# /oreon:deps
%description
Engine for use FIGlet fonts to rendering text.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c

cp %{SOURCE1} .

cd %{pear_name}-%{version}
# Fix wrong-file-end-of-line-encoding
sed -e 's/\r//' -i docs/README.TXT
# Remove checksum for altered files
sed -e '/README.TXT/s/md5sum=.*name/name/' \
    ../package.xml >%{name}.xml

%build

cd %{pear_name}-%{version}
%install
rm -rf %{buildroot}
cd %{pear_name}-%{version}
%{__pear} install --nodeps --packagingroot %{buildroot} %{name}.xml
rm -rf %{buildroot}%{pear_metadir}/.??*
mkdir -p %{buildroot}%{pear_xmldir}
install -pm 644 %{name}.xml %{buildroot}%{pear_xmldir}
%oreon_autofiles main

%post

%{__pear} install --nodeps --soft --force --register-only \
    %{pear_xmldir}/%{name}.xml >/dev/null || :
%postun

if [ $1 -eq 0 ] ; then
    %{__pear} uninstall --nodeps --ignore-errors --register-only \
        pear.php.net/%{pear_name} >/dev/null || :
fi
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
