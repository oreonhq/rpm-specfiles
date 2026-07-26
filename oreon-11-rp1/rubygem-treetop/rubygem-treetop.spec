%global source0_hash 23e8bff4cbcd855120f858609a1fc70d84f45a001bb6f31dd9401816cc64e69b

%global gem_name treetop

Name: rubygem-%{gem_name}
Version: 1.6.12
Release: 9%{?dist}
Summary: A Ruby-based text parsing and interpretation DSL
License: MIT
URL: https://github.com/cjheath/treetop
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/cjheath/treetop.git && cd treetop
# git archive -v -o treetop-%%{version}-specs.tar.gz v%%{version} spec/
Source1: %{gem_name}-%{version}-specs.tar.gz
# https://github.com/cjheath/treetop/issues/61
# https://github.com/cjheath/treetop/commit/b12a87d665c180346e356cd9cb0a61512b883b4d
# Replace Kernel#open with pipe usage with IO#popen
# Former usage is removed in ruby4_0
Patch0:  treetop-gh61-IO_popen-ruby40.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(activesupport)
BuildRequires: rubygem(polyglot)
BuildRequires: rubygem(rr)
BuildRequires: rubygem(rspec)
BuildArch: noarch

%description
A Parsing Expression Grammar (PEG) Parser generator DSL for Ruby.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b 1
(
cd %{_builddir}
%patch -P0 -p1
)

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

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{gem_instdir}/doc/tt.1 %{buildroot}%{_mandir}/man1

%check
pushd .%{gem_instdir}
ln -s %{_builddir}/spec spec
rspec spec
popd

%files
%dir %{gem_instdir}
%{_bindir}/tt
%license %{gem_instdir}/LICENSE
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%doc %{_mandir}/man1/*

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/History.txt
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
# TextMate Bundle? Really?
# https://github.com/cjheath/treetop/pull/34
%exclude %{gem_instdir}/Treetop.tmbundle
%doc %{gem_instdir}/doc
%{gem_instdir}/examples
%{gem_instdir}/treetop.gemspec

%changelog
%autochangelog
