%global source0_hash 8115af8f2b7d120456e97dac3bd284a5b512d48d1ab8494a4942e566d6cfb0e2

%{!?pear_metadir: %global pear_metadir %{pear_phpdir}}
%{!?__pear: %{expand: %%global __pear %{_bindir}/pear}}
%global pear_name PEAR_Command_Packaging

Name:           php-pear-PEAR-Command-Packaging
Version:        0.3.0
Release:        32%{?dist}
Summary:        Create RPM spec files from PEAR modules

# Automatically converted from old format: PHP - review is highly recommended.
License:        PHP-3.01
URL:            http://pear.php.net/package/PEAR_Command_Packaging
Source0:        http://pear.php.net/get/%{pear_name}-%{version}.tgz
Source1:        php-pear-PEAR-Command-Packaging-fedora-template-specfile
Patch0:         php-pear-PEAR-Command-Packaging-0.3.0-fedora-conventions.patch
# https://pear.php.net/bugs/19673 - Adaptation required for metadata_dir
Patch1:         php-pear-PEAR-Command-Packaging-0.3.0-metadata.patch
Patch2:         php-pear-PEAR-Command-Packaging-0.3.0-metadata2.patch

BuildArch:      noarch
BuildRequires:  php-pear

Requires:       php-pear(PEAR)
Requires(post): %{__pear}
Requires(postun): %{__pear}
Provides:       php-pear(%{pear_name}) = %{version}

%description
This command is an improved implementation of the standard PEAR "makerpm" 
command, and contains several enhancements that make it far more flexible. 
Similar functions for other external packaging mechanisms may be added at
a later date.

This package generate spec file closed to fedora PHP Guidelines:
http://fedoraproject.org/wiki/Packaging:PHP

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c

cd %{pear_name}-%{version}
mv ../package.xml %{name}.xml

# Patches for Fedora conventions
%patch -P0 -p1 -b .fedora
# Patches for new Metadata location
%patch -P1 -p1 -b .metadata
%patch -P2 -p1 -b .metadata2

%build
# Empty build section, nothing required

%install
cd %{pear_name}-%{version}
rm -rf %{buildroot}
%{__pear} install --nodeps --packagingroot %{buildroot} %{name}.xml

cp -p %{SOURCE1} %{buildroot}%{pear_datadir}/%{pear_name}/template.spec

# Clean up unnecessary files
rm -rf %{buildroot}%{pear_metadir}/.??*

# Install XML package description
mkdir -p %{buildroot}%{pear_xmldir}
install -pm 644 %{name}.xml %{buildroot}%{pear_xmldir}

%post
%{__pear} install --nodeps --soft --force --register-only \
    %{pear_xmldir}/%{name}.xml >/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    %{__pear} uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi

%files
%doc %{pear_docdir}/%{pear_name}
%{pear_xmldir}/%{name}.xml
%{pear_datadir}/%{pear_name}
%{pear_testdir}/%{pear_name}
%{pear_phpdir}/PEAR/Command/Packaging.*

%changelog
%autochangelog
