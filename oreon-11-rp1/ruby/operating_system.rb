module Gem
  class << Gem
    def default_dir
      @default_dir ||= File.join(RbConfig::CONFIG['datadir'], 'gems')
    end

    def default_ext_dir_for(base_dir)
      return unless base_dir == default_dir
      File.join(RbConfig::CONFIG['libdir'], 'gems', 'ruby')
    end
  end
end
