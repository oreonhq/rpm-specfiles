%global source0_hash bfc3ce5cecd27d940a415de5b557321cf7494058dd878bbef9a8d6186d8000fb

%global gem_name ox

Name:           rubygem-%{gem_name}
Version:        2.14.17
Release:        9%{?dist}
Summary:        Fast XML parser and object serializer

License:        MIT
URL:            http://www.ohler.com/ox
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/ohler55/ox && cd ox
# git archive -v -o rubygem-ox-2.14.17-repo.tgz v2.14.17 test/ examples/
Source1:        %{name}-%{version}-repo.tgz

BuildRequires:  gcc
BuildRequires:  rubygems-devel
BuildRequires:  ruby-devel
BuildRequires:  rubygem(bigdecimal)
BuildRequires:  rubygem(test-unit)
# not automagically detected (from the compiled part)
Requires:       rubygem(bigdecimal)

%description
A fast XML parser and object serializer that uses only standard C lib.
Optimized XML (Ox), as the name implies was written to provide speed optimized
XML handling. It was designed to be an alternative to Nokogiri and other Ruby
XML parsers for generic XML parsing and as an alternative to Marshal for
Object serialization.

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version} -a1

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

# fix shebang in examples
sed -i -e '1 s,#!/usr/bin/env ruby,#!/usr/bin/ruby,' examples/*

%build
gem build %{gem_name}.gemspec

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}/ox
cp -a .%{gem_extdir_mri}/gem.build_complete %{buildroot}%{gem_extdir_mri}/
cp -a .%{gem_extdir_mri}/*.so %{buildroot}%{gem_extdir_mri}/ox/
rm -rf %{buildroot}%{gem_instdir}/ext/

# examples - script interpreter, not executable
cp -a examples/ %{buildroot}%{gem_instdir}
sed -i -e 's|/usr/bin/env ruby|/usr/bin/ruby|' %{buildroot}%{gem_instdir}/examples/*
chmod -x %{buildroot}%{gem_instdir}/examples/*

%check
cp -pr test/ ./%{gem_instdir}
pushd ./%{gem_instdir}
ruby -Ilib:test:%{buildroot}%{gem_extdir_mri} test/tests.rb
ruby -Ilib:test:%{buildroot}%{gem_extdir_mri} test/sax/sax_test.rb
rm -rf test/
popd

%files
%dir %{gem_instdir}/
%license %{gem_instdir}/LICENSE
%{gem_extdir_mri}/
%{gem_libdir}/
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}/
%doc %{gem_instdir}/examples/
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
%autochangelog
