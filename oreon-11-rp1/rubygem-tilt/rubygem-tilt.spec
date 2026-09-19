%global source0_hash 74cb9e852673f6f2b90126cb24abe6da4dbedea07f68d45eb1f47e6b1c975c55

%global gem_name tilt

# When we are bootstrapping, we drop some dependencies, and/or build time tests.
%bcond_with bootstrap

Name: rubygem-%{gem_name}
Version: 2.2.0
Release: 8%{?dist}
Summary: Generic interface to multiple Ruby template engines
License: MIT
URL: https://github.com/jeremyevans/tilt
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Man pages were dropped by upstream :'(
# https://github.com/jeremyevans/tilt/issues/7
## git clone https://github.com/jeremyevans/tilt.git && cd tilt
## git archive -v -o tilt-2.2.0-man.tar.gz v2.2.0 man/
#Source1: %%{gem_name}-%%{version}-man.tar.gz

# git clone https://github.com/jeremyevans/tilt.git && cd tilt
# git archive -v -o tilt-2.2.0-test.tar.gz v2.2.0 test/
Source2: %{gem_name}-%{version}-test.tar.gz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
# These templating engines are removed or deprecated in Fedora.
# BuildRequires: rubygem(coffee-script)
# BuildRequires: rubygem(erubis)
# BuildRequires: rubygem(maruku)
# BuildRequires: rubygem(wikicloth)
BuildRequires: rubygem(creole)
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(minitest-mock)
BuildRequires: rubygem(nokogiri)
BuildRequires: rubygem(erubi)
BuildRequires: rubygem(builder)
BuildRequires: rubygem(RedCloth)
BuildRequires: rubygem(redcarpet)
BuildRequires: rubygem(kramdown)
BuildRequires: rubygem(rdiscount)
BuildRequires: rubygem(sassc)
BuildRequires: rubygem(asciidoctor)
BuildRequires: rubygem(prawn)
BuildRequires: rubygem(pdf-reader)
%if %{without bootstrap}
BuildRequires: rubygem(haml)
BuildRequires: rubygem(slim)
%endif
## To generate man pages.
#BuildRequires: /usr/bin/ronn
BuildArch: noarch

%description
Generic interface to multiple Ruby template engines.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b 2

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

# Fix shebang.
sed -i -e 's|/usr/bin/env ruby|/usr/bin/ruby|' %{buildroot}%{gem_instdir}/bin/tilt

## Generate man pages.
#pushd %{_builddir}
#  ronn --manual="Tilt Manual" --organization="Tilt %{version}" -r man/*.ronn
#
#  mkdir -p %{buildroot}%{_mandir}/man1
#  mv man/*.1 %{buildroot}%{_mandir}/man1
#popd

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%if %{without bootstrap}
%check
pushd .%{gem_instdir}
cp -a %{_builddir}/test test

LANG=C.UTF-8 ruby -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd
%endif

%files
%dir %{gem_instdir}
%{_bindir}/tilt
%license %{gem_instdir}/COPYING
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
#%%doc %%{_mandir}/man1/*

%files doc
%doc %{gem_docdir}

%changelog
%autochangelog
