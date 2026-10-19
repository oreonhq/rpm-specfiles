%global source0_hash b310cc0a040828d0b0b4b796d43b425ecaa8b10fa7c78b20712867d6fd3c6b20
%{!?pear_metadir: %global pear_metadir %{pear_phpdir}}
%{!?__pear: %{expand: %%global __pear %{_bindir}/pear}}
%global pear_name Image_Text
Name:           php-pear-Image-Text
Version:        0.7.0
Release:        1%{?dist}
Summary:        Advanced text manipulations in images
License:        PHP-3.01
URL:            http://pear.php.net/package/Image_Text
Source0:        %{pear_name}-%{version}-strip.tgz
Source1:        strip.sh
BuildArch:      noarch
Requires(post): %{__pear}
Requires(postun): %{__pear}
Requires:       php-gd
Requires:       php-pcre
Requires:       php-pear(PEAR)
Provides:       php-pear(%{pear_name}) = %{version}
# oreon:deps
BuildRequires:  php-pear(PEAR)
# /oreon:deps
%description
%{pear_name} provides a comfortable interface to text manipulations in GD
images. Beside common Freetype2 functionality it offers to handle texts
in a graphic- or office-tool like way. For example it allows alignment of
texts inside a text box, rotation (around the top left corner of a text
box or it's center point) and the automatic measurement of the optimal
font size for a given text box.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c

cd %{pear_name}-%{version}
mv ../package.xml %{name}.xml

%build

cd %{pear_name}-%{version}
%install
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
