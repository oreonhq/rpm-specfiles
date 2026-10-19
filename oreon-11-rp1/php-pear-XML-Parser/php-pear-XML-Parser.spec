%global source0_hash d78f47fc0de35dc05a203a77f54c0ea03db1f48592c345dde8b4893fb64980eb
%{!?__pear: %global __pear %{_bindir}/pear}
%global pear_name   XML_Parser
%global with_tests  %{?_with_tests:1}%{!?_with_tests:0}
Name:         php-pear-XML-Parser
Version:      1.3.8
Release:        1%{?dist}
Summary:        XML parsing class based on PHP's bundled expat
Summary(fr):  Une classe d'analyse XML utilisant l'extension expat de PHP
License:      LicenseRef-Callaway-BSD
URL:          http://pear.php.net/package/XML_Parser
Source0:        http://pear.php.net/get/%{pear_name}-%{version}.tgz
BuildArch:        noarch
%if %{with_tests}
%endif
Requires(post):   %{__pear}
Requires(postun): %{__pear}
Requires:         php-pear(PEAR) >= 1.4.9
Provides:         php-pear(%{pear_name}) = %{version}
Provides:         php-composer(pear/xml_parser) = %{version}
# oreon:deps
BuildRequires:  php-pear
# /oreon:deps
%description
This is an XML parser based on PHPs built-in xml extension.
It supports two basic modes of operation: "func" and "event".  
In "func" mode, it will look for a function named after each element 
(xmltag_ELEMENT for start tags and xmltag_ELEMENT_ for end tags), 
and in "event" mode it uses a set of generic callbacks.

Since version 1.2.0 there's a new XML_Parser_Simple class that makes 
parsing of most XML documents easier, by automatically providing a stack 
for the elements. Furthermore its now possible to split the parser from 
the handler object, so you do not have to extend XML_Parser anymore in 
order to parse a document with it.

%description -l fr
Une analyseur XML utilisant l'extension xml intégrée à PHP.
Il supporte deux simples modes de fonctionnement : "func" et "event".
Dans le mode "func", il cherche une fonction nommée après chaque élément
(xmltag_ELEMENT pour le drapeau de début et xmltag_ELEMENT_ pour celui
de fin), et dans le mode "event" il utilise en ensemble de fonctions
"callbacks" génériques.

Depuis la version 1.2.0, la nouvelle classe XML_Parser_Simple simplifie
l'analyse de la plupart des documents XML, en fournissant automatiquement
une pile pour les éléments. De plus il est désormais possible de séparer
l'analyseur du gestionnaire d'objets, il n'est donc plus nécessaire d'étendre
XML_Parser pour analyser un document.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c

cd %{pear_name}-%{version}
# package.xml is V2
mv ../package.xml %{name}.xml

%build

%install
cd %{pear_name}-%{version}
%{__pear} install --nodeps --packagingroot %{buildroot} %{name}.xml
rm -rf %{buildroot}%{pear_metadir}/.??*
install -Dpm 644 %{name}.xml %{buildroot}%{pear_xmldir}/%{name}.xml
for file in  %{buildroot}%{pear_docdir}/%{pear_name}/examples/*; do
  sed -i -e 's/\r//' $file
done
%oreon_autofiles main

%check

%if %{with_tests}
cd %{pear_name}-%{version}
%{__pear} \
   run-tests \
   -i "-d include_path=%{buildroot}%{pear_phpdir}:%{pear_phpdir}" \
   tests | tee ../testslog
grep "FAILED TESTS" ../testslog && exit 1
%endif
%post

%{__pear} install --nodeps --soft --force --register-only %{pear_xmldir}/%{name}.xml >/dev/null || :
%postun

if [ "$1" -eq "0" ]; then
    %{__pear} uninstall --nodeps --ignore-errors --register-only %{pear_name} >/dev/null || :
fi
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
