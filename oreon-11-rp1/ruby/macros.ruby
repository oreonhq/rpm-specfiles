%ruby_version @@RUBY_VERSION@@
%ruby_abi @@RUBY_ABI@@
%ruby_arch @@RUBY_ARCH@@

%ruby_libdir %{_libdir}/ruby/%{ruby_abi}
%ruby_libarchdir %{ruby_libdir}/%{ruby_arch}

%ruby_vendordir vendor_ruby
%ruby_vendorlibdir %{_libdir}/ruby/%{ruby_vendordir}/%{ruby_abi}
%ruby_vendorarchdir %{ruby_vendorlibdir}/%{ruby_arch}

%ruby_sitedir site_ruby
%ruby_sitelibdir %{_prefix}/local/lib64/ruby/%{ruby_sitedir}/%{ruby_abi}
%ruby_sitearchdir %{ruby_sitelibdir}/%{ruby_arch}

%ruby_default_gemdir %{_libdir}/ruby/gems/%{ruby_abi}
