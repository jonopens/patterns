class FormData
  attr_accessor :validation_strategy

  def initialize(validation_strategy)
    @validation_strategy = validation_strategy
  end
end

class ValidationStrategy
  def validate(string)
    raise "That's not right! Way to ruin my abstraction :[ "
  end
end

class URLValidationStrategy < ValidationStrategy
  def initialize(separator)
    @separator = separator
  end

  def validate(string)
    
  end
end

class ValidationStrategy < ValidationStrategy
  def initialize(separator)
    @separator = separator
  end

  def validate(string)
    
  end
end