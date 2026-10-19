%global source0_hash ab241cadfb3fd4fe8ba5e3db4958fbe000039e51c14b79d0b420da3dab35789f
%{!?pear_metadir: %global pear_metadir %{pear_phpdir}}
%{!?__pear: %{expand: %%global __pear %{_bindir}/pear}}
%global pear_name File_Fstab
Name:           php-pear-File-Fstab
Version:        2.0.3
Release:        27%{?dist}
Summary:        Read and write fstab files
License:        PHP-3.01
URL:            http://pear.php.net/package/File_Fstab
Source0:        http://pear.php.net/get/%{pear_name}-%{version}.tgz
Source1:        LICENSE
BuildArch:      noarch
Requires(post): %{__pear}
Requires(postun): %{__pear}
Requires:       php-pear(PEAR)
Requires:       php-pcre
Provides:       php-pear(%{pear_name}) = %{version}
# oreon:deps
BuildRequires:  php-pear(PEAR)
# /oreon:deps
%description
File_Fstab is an easy-to-use package which can read & write UNIX fstab
files. It presents a pleasant object-oriented interface to the fstab.
Features:
* Supports blockdev, label, and UUID specification of mount device.
* Extendable to parse non-standard fstab formats by defining a new Entry
class for that format.
* Easily examine and set mount options for an entry.
* Stable, functional interface.
* Fully documented with PHPDoc.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c

cp %{SOURCE1} LICENSE

cd %{pear_name}-%{version}
# https://pear.php.net/bugs/bug.php?id=19781
sed -e '/Makefile/d' \
    -e '/example.php/s/role="php"/role="doc"/' \
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
