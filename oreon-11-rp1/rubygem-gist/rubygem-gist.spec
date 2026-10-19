%global source0_hash 0d0a3616b1a4eec837ce4e5b5477bc809d58597ee350b2c34104acd3b00ccd62
%global gem_name gist
Name: rubygem-%{gem_name}
Version: 6.0.0
Release:        1%{?dist}
Summary:        Upload content to https://gist.github.com
License: MIT
URL: https://github.com/defunkt/gist
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildArch: noarch
# oreon:deps
BuildRequires:  /usr/bin/ronn
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygem(webmock)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Upload source code, text files and similar content to https://gist.github.com
or a local GitHub Enterprise instance.

This package provides the gist command line utility and a single function
(Gist.gist) that uploads a gist.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}

%build

gem build ../%{gem_name}-%{version}.gemspec
sed  's/\xe2\x80\x8c/\* /g' README.md > README.md.ron
ronn --roff --manual="Gist manual" README.md.ron
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
cp README.md.1 %{buildroot}%{_mandir}/man1/%{gem_name}.1
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
rspec spec
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-gist-doc -f %{oreon_filedir}/rubygem-gist-doc.list

%changelog

%autochangelog
