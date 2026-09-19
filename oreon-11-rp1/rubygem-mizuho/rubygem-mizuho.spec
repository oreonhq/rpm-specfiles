%global source0_hash 7af8f0033c87939fbc15ca01422fc6159cf654baf0995b11c72e543d2977f8d8

%global gem_name mizuho
# Although there are tests, they don't work yet
# https://github.com/FooBarWidget/mizuho/issues/5
%global enable_tests 0

Summary:       Mizuho documentation formatting tool
Name:          rubygem-%{gem_name}
Version:       0.9.20
Release:       26%{?dist}
License:       MIT
URL:           https://github.com/FooBarWidget/mizuho
Source0:       https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch1:        rubygem-mizuho-0.9.20-fix_native_templates_dir.patch
Requires:      asciidoc
Requires:      ruby(release)
Requires:      ruby(rubygems) 
Requires:      rubygem(nokogiri) >= 1.4.0
Requires:      rubygem(sqlite3) 
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
%if 0%{?enable_tests}
BuildRequires: rubygem-rspec
%endif
BuildArch:     noarch
Provides:      rubygem(%{gem_name}) = %{version}

%description
A documentation formatting tool. Mizuho converts Asciidoc input files into
nicely outputted HTML, possibly one file per chapter. Multiple templates are
supported, so you can write your own.

%package doc
Summary:   Documentation for %{name}
Requires:  %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gem unpack %{SOURCE0}
%setup -q -D -T -n  %{gem_name}-%{version}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

# Unbundle asciidoc
rm -rf asciidoc
sed -i 's/NATIVELY_PACKAGED = .*/NATIVELY_PACKAGED = true/' lib/mizuho.rb
sed -i -e 's\ "asciidoc[^,]*,\\g' %{gem_name}.gemspec

# Fixup rpmlint failures
echo "#toc.html" >> templates/toc.html

%patch -P1 -p 1

%build
gem build %{gem_name}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -a ./%{_bindir}/* %{buildroot}%{_bindir}

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

# Remove build leftovers.
rm -rf %{buildroot}%{gem_instdir}/{.rvmrc,.document,.require_paths,.gitignore,.travis.yml,rpm,.rspec,.gemtest,.yard*}
rm -rf %{buildroot}%{gem_instdir}/%{gem_name}.gemspec

%if 0%{?enable_tests}
%check
pushd %{buildroot}%{gem_instdir}
ruby -Ilib -S rspec -f s -c test/*_spec.rb
popd
%endif

%files
%doc %{gem_instdir}/LICENSE.txt
%dir %{gem_instdir}
%{_bindir}/mizuho
%{_bindir}/mizuho-asciidoc
%{gem_instdir}/bin
%{gem_instdir}/debian.template
%{gem_instdir}/source-highlight
%{gem_instdir}/templates
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_instdir}/README.markdown
%doc %{gem_docdir}
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
%autochangelog
